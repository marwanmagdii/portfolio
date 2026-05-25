import os
import fitz  # PyMuPDF
import re

BASE_DIR = r'D:\web\portfolio entrepreneur\assets\certifications'

# 1. Convert PDFs to JPGs
pdf_files = [f for f in os.listdir(BASE_DIR) if f.lower().endswith('.pdf')]

for pdf_file in pdf_files:
    pdf_path = os.path.join(BASE_DIR, pdf_file)
    jpg_file = pdf_file[:-4] + '.jpg'
    jpg_path = os.path.join(BASE_DIR, jpg_file)
    
    if not os.path.exists(jpg_path):
        print(f"Converting {pdf_file} to JPG...")
        try:
            doc = fitz.open(pdf_path)
            # Render first page at high resolution (approx 300 DPI)
            page = doc.load_page(0)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            pix.save(jpg_path)
            doc.close()
        except Exception as e:
            print(f"Error converting {pdf_file}: {e}")

# 2. Update rebuild_certs.py to point to JPGs instead of PDFs
REBUILD_SCRIPT = r'D:\web\portfolio entrepreneur\rebuild_certs.py'
with open(REBUILD_SCRIPT, 'r', encoding='utf-8') as f:
    rebuild = f.read()

# The rebuild script uses CERTS array which has "pdf": "assets/certifications/....pdf"
# We need to change all .pdf extensions in the CERTS JSON string to .jpg
# But wait, rebuild_certs.py imports CERTS from certs_data.py now?
# "from certs_data import CERTS"
# Yes! Let's check if certs_data.py exists and update it there.

CERTS_DATA = r'D:\web\portfolio entrepreneur\certs_data.py'
if os.path.exists(CERTS_DATA):
    with open(CERTS_DATA, 'r', encoding='utf-8') as f:
        data = f.read()
    
    # Replace .pdf with .jpg
    data = data.replace('.pdf', '.jpg')
    data = data.replace('.PDF', '.jpg')
    
    with open(CERTS_DATA, 'w', encoding='utf-8') as f:
        f.write(data)
    print("Updated certs_data.py")
else:
    print("certs_data.py not found, updating rebuild_certs.py directly if needed.")
    rebuild = rebuild.replace('.pdf', '.jpg')
    with open(REBUILD_SCRIPT, 'w', encoding='utf-8') as f:
        f.write(rebuild)

# 3. Rebuild certifications.html
import subprocess
print("Rebuilding certifications HTML...")
subprocess.run(['python', 'rebuild_certs.py'], cwd=r'D:\web\portfolio entrepreneur')
print("Done!")
