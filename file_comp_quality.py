# Определить, какой файл в архиве имеет наилучшую степень сжатия
from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    comp_qty = {
        elem.filename.split('/')[-1]: elem.file_size / elem.compress_size
        for elem in file.infolist() if not elem.is_dir()
    }
    print(max(comp_qty, key=lambda a:comp_qty[a]))
