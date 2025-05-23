from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
from odoo_client import create_odoo_lead
from pdf_generator import generate_pdf_report
import uuid
import os

app = FastAPI()

@app.post("/intake")
async def handle_intake(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    damage_description: str = Form(...),
    declaration_file: UploadFile = File(...),
    photo_files: list[UploadFile] = File(...)
):
    intake_id = str(uuid.uuid4())
    os.makedirs(f"intake/{intake_id}", exist_ok=True)
    dec_path = f"intake/{intake_id}/declaration.pdf"
    with open(dec_path, "wb") as f:
        f.write(await declaration_file.read())

    photo_paths = []
    for i, photo in enumerate(photo_files):
        path = f"intake/{intake_id}/photo_{i}.jpg"
        with open(path, "wb") as f:
            f.write(await photo.read())
        photo_paths.append(path)

  report_path = f"intake/{intake_id}/report.pdf"
generate_pdf_report(name, damage_description, photo_paths, output_path=report_path)

report_url = f"/report/{intake_id}"
print("✅ Intake ID:", intake_id)
print("📄 Report path:", report_path)
print("✅ Generated report URL:", report_url)

return {
    "status": "ok",
    "report_url": report_url
}


@app.get("/report/{intake_id}")
def get_report(intake_id: str):
    return FileResponse(f"intake/{intake_id}/report.pdf")
