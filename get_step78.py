import re

log_path = r'C:\Users\MARWAN MAGDY\.gemini\antigravity\brain\20b574b2-2900-4802-8c8d-acb3fd0bcf23\.system_generated\logs\overview.txt'
with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's find step 78 block by searching for "step_index":78
# and then find the string value of "CodeContent"
start_str = '"step_index":78'
idx = text.find(start_str)
if idx != -1:
    print("Found step 78 at index:", idx)
    # Search for CodeContent inside this block
    code_start = text.find('"CodeContent":', idx)
    if code_start != -1:
        # Find the opening quote
        quote_start = text.find('"', code_start + len('"CodeContent":'))
        # Find the closing quote of CodeContent. We need to handle escaped quotes inside the string.
        # The string ends with ", so we scan character by character
        code_str = ""
        i = quote_start + 1
        escaped = False
        while i < len(text):
            char = text[i]
            if escaped:
                code_str += char
                escaped = False
            elif char == '\\':
                escaped = True
                code_str += char
            elif char == '"':
                # This is the end quote
                break
            else:
                code_str += char
            i += 1
        print("Extracted code length:", len(code_str))
        # Now let's decode the string escape sequence
        # We can do this by using codec 'unicode_escape' or json.loads
        try:
            decoded = bytes(code_str, "utf-8").decode("unicode_escape")
            # Wait, unicode_escape might fail or decode too much if there are other escapes,
            # but let's try json.loads of '"' + code_str + '"'
            import json
            decoded = json.loads('"' + code_str + '"')
            with open('about_step78.html', 'w', encoding='utf-8') as out:
                out.write(decoded)
            print("Successfully wrote decoded HTML to about_step78.html")
        except Exception as e:
            print("Failed decoding:", e)
            # fallback: just write the raw code_str
            with open('about_step78_raw.html', 'w', encoding='utf-8') as out:
                out.write(code_str)
            print("Wrote raw string to about_step78_raw.html")
