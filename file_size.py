from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    bef_size, aft_size = 0, 0
    for elem in file.infolist():
        bef_size += elem.file_size
        aft_size += elem.compress_size
    print(f'Объем исходных файлов: {bef_size} байт(а)')
    print(f'Объем сжатых файлов: {aft_size} байт(а)')
