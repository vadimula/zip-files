from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    qtty = [True for elem in file.infolist() if not elem.is_dir()]
    print(len(qtty))
