from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    print(sum([not elem.is_dir() for elem in file.infolist()]))
