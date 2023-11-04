import json
from datetime import datetime

with open('file1.txt', 'r', encoding='utf-8') as file:
    data = list(file.readlines())
res = {}
for line in data:
    if line[:2].isdigit():
        rec_data = str(datetime.strptime(line.strip(), '%d.%m.%Y; %H:%M'))
        res.setdefault(rec_data, [])
    elif line.strip():
        res.setdefault(rec_data, []).append(line.strip())

with open('file1.json', 'w', encoding='utf-8') as file:
    json.dump(res, file, indent=3, ensure_ascii=False)