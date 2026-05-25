import os

BASE = r'D:\web\portfolio entrepreneur'
SCRIPT = os.path.join(BASE, 'rebuild_certs.py')

with open(SCRIPT, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace onclick="close()" with onclick="closeModal()"
code = code.replace('onclick="close()"', 'onclick="closeModal()"')
# Replace the function declaration
code = code.replace('function close(){', 'function closeModal(){')
# Replace the event listener for escape key
code = code.replace("if(e.key==='Escape')close();", "if(e.key==='Escape')closeModal();")
# Replace the overlay onclick
code = code.replace('onclick="if(event.target===this)close()"', 'onclick="if(event.target===this)closeModal()"')

with open(SCRIPT, 'w', encoding='utf-8') as f:
    f.write(code)

import subprocess
subprocess.run(['python', 'rebuild_certs.py'], cwd=BASE)
print("Modal close fixed and rebuilt.")
