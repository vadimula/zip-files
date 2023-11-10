# Функция должна извлекать файлы *args из архива zip_name в папку с программой.
# Если в функцию не передано ни одного названия файла для извлечения, то функция должна извлечь все файлы из архива.
from zipfile import ZipFile

file_names = ['aaa.txt', 'bbb.txt', 'ccc.txt']
arch_name = 'files.zip'
def extract_this(file_names, arch_name):
    with ZipFile(arch_name, mode='w') as zip_file:
        [zip_file.write(name) for name in file_names]

extract_this(file_names, arch_name)