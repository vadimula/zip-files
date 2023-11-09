#Вам доступен набор различных файлов, названия которых представлены в списке file_names. Также вам доступен архив files.zip.
#Дополните приведенный ниже код, чтобы он добавил в архив files.zip только те файлы из списка file_names, объем которых не превышает 100 байт.
from zipfile import ZipFile
from os.path import getsize

file_names = ['aaa.txt', 'bbb.txt', 'ccc.txt', 'diary.txt']
arch_name = 'files.zip'
def add_arc(file_names, arch_name):
    with ZipFile(arch_name, mode='a') as zip_file:
        [zip_file.write(name) for name in file_names if getsize(name) < 100]

add_arc(file_names, arch_name)