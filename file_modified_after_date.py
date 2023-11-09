# Напишите программу, которая выводит названия всех файлов из этого архива в лексикографическом порядке,
# указывая для каждого его дату изменения, а также объем до и после сжатия.
from zipfile import ZipFile
from datetime import datetime
with ZipFile('workbook.zip') as archive:
    file_names = {
        elem.filename.split('/')[-1]:
            (elem.date_time, elem.file_size, elem.compress_size)
        for elem in archive.infolist()
        if not elem.is_dir()
    }
for name in sorted(file_names):
    print(name)
    print(f'  Дата модификации файла: {datetime(*file_names[name][0])}')
    print(f'  Объем исходного файла:  {file_names[name][1]} байт(а)')
    print(f'  Объем сжатого файла:  {file_names[name][2]} байт(а)')
    print()