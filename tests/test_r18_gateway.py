"""Real published R18 AI gateway E2E, with a synthetic 39-scene ZIP."""
import hashlib
import json
import struct
import tempfile
import zlib
import zipfile
from pathlib import Path
from playwright.sync_api import sync_playwright

URL="https://mrs-zhong1.github.io/motion-studio-web-pages/review-r18-ai.html"
COUNTS={"editorial":4,"product-3d":5,"cinematic":5,"architecture":5,
        "agency":5,"fashion":5,"gallery":5,"saas":5}

def png(r,g,b):
    def chunk(t,data):
        return struct.pack("!I",len(data))+t+data+struct.pack("!I",zlib.crc32(t+data)&0xffffffff)
    pixels=b"".join(b"\0"+bytes([r,g,b])*24 for _ in range(24))
    image=b"\x89PNG\r\n\x1a\n"+chunk(b'IHDR',struct.pack("!2I5B",24,24,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(pixels))+chunk(b'IEND',b'')
    return image+bytes([r])*1400

def pack(directory):
    archive=directory/"ai-test.zip"
    rows=[]
    with zipfile.ZipFile(archive,"w",compression=zipfile.ZIP_DEFLATED) as z:
        for template,count in COUNTS.items():
            for chapter in range(1,count+1):
                name=f"{template}-{chapter}.png"
                data=png((chapter*47+len(template))%256,(chapter*19)%256,((len(template)+chapter)*23)%256)
                rows.append(dict(template=template,chapter=chapter,file=name,
                       source="AI_GENERATED",commercialUseTermsChecked=True,
                       sha256=hashlib.sha256(data).hexdigest()))
                z.writestr("stage9/ai-assets/"+name,data)
        z.writestr("stage9/ai-assets/manifest.json",json.dumps({"assets":rows}))
        z.writestr("release/R18_ASSET_TECHNICAL_AUDIT.json","{}")
    return archive

def test_gateway():
    with tempfile.TemporaryDirectory() as tmp:
        archive=pack(Path(tmp))
        with sync_playwright() as pw:
            browser=pw.chromium.launch(headless=True,args=["--no-sandbox"])
            page=browser.new_page(viewport={"width":1440,"height":900})
            errors=[]
            page.on("pageerror",lambda e:errors.append(str(e)))
            page.goto(URL,wait_until="domcontentloaded",timeout=60000)
            frame=page.frame_locator("#app")
            frame.locator("[data-template-card]").first.wait_for(timeout=90000)
            assert frame.locator("[data-template-card]").count()==8
            page.locator("#pack").set_input_files(str(archive))
            page.wait_for_function("""() => document.querySelector('#status').textContent.includes('39/39') || document.querySelector('#status').textContent.includes('导入失败')""",timeout=60000)
            final_status=page.locator("#status").text_content()
            print("R18 ZIP gateway status:",final_status,flush=True)
            assert "39/39" in final_status,final_status
            assert frame.locator("[data-template-card]").count()==8
            source=frame.locator("body").evaluate("""async()=>{
               await ensureTemplatePhoto('editorial');
               return {count:templateAssetAuditCache.get('editorial').length,
                 kinds:templateAssetAuditCache.get('editorial').map(x=>x.kind),
                 cover:templateThumbnailImages.editorial.slice(0,22),
                 components:registry.length}
            }""")
            assert source["count"]==4 and source["kinds"]==["ai-generated-image"]*4,source
            assert source["cover"].startswith("data:image/png"),source
            assert source["components"]==20,source
            frame.locator("[data-template-card='editorial']").click()
            frame.locator("#previewUse").click()
            assert frame.locator("#editorView").is_visible()
            assert not errors,errors
            print(json.dumps({"status":"PASS","templates":8,"AI":39,"components":20,
                              "engine":"Chromium real GitHub Pages","source":source}))
            browser.close()
if __name__=="__main__":
    test_gateway()
