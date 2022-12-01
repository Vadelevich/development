import csv


def get_by_date_1(date="2017-08-08", name="PCLN", filename='dump.csv'):
    """Функция создает словарь по названию тикера, потребляет память O(n) , зато выполняет поиск О(1) """
    with open(f'{filename}', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Name'] == name:  # Создаем словарик по аттрибуту name
                graph.update(
                    {row['date']: [row['open'], row['high'], row['low'], row['close'], row['volume'], row['Name']]})
        with open('my_file.csv', mode='a') as outfile:
            writer = csv.writer(outfile, delimiter='|')
            writer.writerow(graph[date])  # Просто ищем по ключу в словаре


def get_by_date_line_find(date="2017-08-08", name="PCLN", filename='dump.csv'):
    """Функция ищет  date, name линейным поиском , не потребляет памяти  """
    with open(f'{filename}', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['date'] == date and row['Name'] == name:
                my_str = [row['date'], row['open'], row['high'], row['low'], row['close'], row['volume'], row['Name']]
                with open('my_file.csv', mode='a') as outfile:
                    writer = csv.writer(outfile, delimiter='|')
                    writer.writerow(my_str)


graph = dict()
get_by_date_line_find(date="2017-08-08", name="PCLN", filename='dump.csv')
get_by_date_1(date="2017-08-08", name="PCLN", filename='dump.csv')
