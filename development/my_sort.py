import csv

slovar_1 = dict()
slovar_2 = dict()
slovar_rez = dict()
def select_sorted(sort_columns=['high'], order='asc', limit=10, filename='all.csv'):
    with open(f'{filename}') as csv_File:
        csv_reader = csv.DictReader(csv_File)
        count_1, count_2 = limit, limit
        for row in csv_reader:
            if count_1 != 0:
                slovar_1.update(
                    {row[sort_columns[0]]:[row['date'], row['open'], row['high'], row['low'], row['close'], row['volume'], row['Name']]})
                count_1 -= 1
            elif count_2 != 0:
                slovar_2.update({row[sort_columns[0]]:[row['date'], row['open'], row['high'], row['low'], row['close'], row['volume'], row['Name']]})
                count_2 -= 1
            else:

                count_1,count_2 = limit, limit
    print(slovar_rez)

    # print(slovar_1)
    # print('********************************************************************************************************')
    # print('********************************************************************************************************')
    # print('********************************************************************************************************')
    # print('********************************************************************************************************')
    # print('********************************************************************************************************')
    # print('********************************************************************************************************')
    # print('********************************************************************************************************')
    # print('********************************************************************************************************')
    # print(slovar_2)






select_sorted(sort_columns=['high'], order='asc', limit=10, filename='all.csv')
# записывает в dump.csv данные из анализируемого файла,
# отсортированные по колонке 'high'
# в порядке возрастания
# первые 10 записей

# ПОИСК (Данные считаем уже отсортированными по дате)
#get_by_date(date="2017-08-08", name="PCLN", filename='dump.csv')
# сохраняет в файл все данные по тикеры "PCLN" за 2017-08-08

# КЭШИРОВАНИЕ
#select_sorted(sort_columns=['high'], order='asc', limit=10, filename='dump3.csv')
# результат берется из "кэша", если запрос повторяется.
