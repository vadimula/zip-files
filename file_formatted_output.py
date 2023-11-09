# Напишите программу, которая выводит названия файлов из этого архива,
# которые были созданы или изменены позднее 2021-11-30 14:22:00.
# Названия файлов должны быть расположены в лексикографическом порядке, каждое на отдельной строке.
from zipfile import ZipFile
with ZipFile('workbook.zip') as archive:
    file_names = [
        elem.filename.split('/')[-1] #                                          Отбираем имена файлов
        for elem in archive.infolist() #                                        из объекта archive
        if not elem.is_dir() and elem.date_time > (2021, 11, 30, 14, 22, 00) #  измененные после даты 30.11.21 г.
    ]
    [print(name) for name in sorted(file_names)] #                              Выводим отсортированный список
