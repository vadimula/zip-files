# Напишите программу, которая выводит названия файлов из этого архива,
# которые были созданы или изменены позднее 2021-11-30 14:22:00.
# Названия файлов должны быть расположены в лексикографическом порядке, каждое на отдельной строке.
from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as archive:
    file_names = [
        elem.filename.split('/')[-1]
        for elem in archive.infolist()
        if not elem.is_dir() and datetime(*elem.date_time) > datetime(2021, 11, 30, 14, 22, 00)
    ]
    [print(name) for name in sorted(file_names)]
