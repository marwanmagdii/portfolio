with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('<!-- ACHIEVEMENT SUMMARY -->')
end = content.find('<!-- CASE STUDIES PREVIEW -->')
if start != -1 and end != -1:
    print(content[start:end])
else:
    print("Could not find section in index.html")
