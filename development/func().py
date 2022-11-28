import pandas as pd

def select_sorted(sort_cols=['high'], order='asc', limit=10, filename='dump.csv'):
    """ Функция сортирует весь файл all.csv по аргументу sort_cols в порядке возвраст.(order) , и записывает первые Limit строки в файл dump.csv """
    data = pd.read_csv("all.csv")   # открываем файл с модулем pandas
    data.sort_values(sort_cols, axis=0, ascending=[ order =='desk'], inplace=True) # сама сортировка, axis - колонки, ascending - порядок
    data.iloc[0 : limit].to_csv(f'{filename}') # iloc - делает срез из pd, to_csv - экспортируем в dump (добавляет индекс строки)

select_sorted(sort_cols=['high'], order='asc', limit=10, filename='dump.csv')