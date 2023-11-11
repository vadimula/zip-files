# Функция должна извлекать файлы *args из архива zip_name в папку с программой.
# Если в функцию не передано ни одного названия файла для извлечения, то функция должна извлечь все файлы из архива.
from zipfile import ZipFile

files = ['aaa.txt', 'bbb.txt', 'ccc.txt']
arch_name = 'files.zip'
def extract_this(arch_name, *files):
    with ZipFile(arch_name, 'r') as archive:
        if files: [archive.extract(name) for name in files]
        else: archive.extractall()

extract_this(arch_name)