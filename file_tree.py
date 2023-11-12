#Вам доступен архив desktop.zip, содержащий различные папки и файлы.
#Напишите программу, которая выводит его файловую структуру и объем каждого файла.
from zipfile import ZipFile

def bytes_conv(x):
    if not x: return ''
    if x < 1025: return f'{str(x)} B'
    if x <= 1024 ** 2: return f'{str(round(x / 1024))} KB'
    return f'{str(round(x / (1024 ** 2)))} MB'

archive = ZipFile('desktop.zip', 'r')
arc_list = archive.namelist()
for name in arc_list:
    row = name.rstrip('/')
    ind = row.rfind('/') + 1
    size = archive.getinfo(name).file_size
    print('  ' * row.count('/') + row[ind:], bytes_conv(size))
archive.close()