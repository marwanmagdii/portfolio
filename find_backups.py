import os

search_dir = r"C:\Users\MARWAN MAGDY\.gemini\antigravity"
found = []
for root, dirs, files in os.walk(search_dir):
    for file in files:
        if 'about' in file.lower() or 'html' in file.lower() or 'resume' in file.lower():
            path = os.path.join(root, file)
            # check size
            try:
                size = os.path.getsize(path)
                if size > 1000:
                    found.append((path, size))
            except:
                pass

print(f"Found {len(found)} candidate files:")
for path, size in found:
    print(f"  {path} ({size} bytes)")
