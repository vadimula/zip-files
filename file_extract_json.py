# Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов,
# выступающих за футбольный клуб Arsenal.

from time import time

from zipfile import ZipFile
import json

a = time()
res = []
with ZipFile('data.zip', 'r') as archive:
    for name in archive.namelist():
        if name.endswith('json'):
            file = archive.open(name)
            try: rows = json.load(file)
            except: pass
            file.close()
            if rows['team'] == 'Arsenal': res.append(rows['first_name'] + ' ' + rows['last_name'])
print(*sorted(res), sep='\n')

print(round((time() - a) * 1000, 2))