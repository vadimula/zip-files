# Вам доступен набор различных файлов, названия которых представлены в списке file_names.
# Дополните приведенный ниже код, чтобы он создал архив files.zip и добавил в него все файлы из данного списка
from zipfile import ZipFile

file_names = ['aaa.txt', 'bbb.txt', 'ccc.txt']
arch_name = 'files.zip'
def make_arc(file_names, arch_name):
    with ZipFile(arch_name, mode='w') as zip_file:
        [zip_file.write(name) for name in file_names]
    print(file_names)
make_arc(file_names, arch_name)