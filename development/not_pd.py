import csv

def cache_args(func):
    """Кеширование не успела доделать, но обязательно доделаю"""
    def wrapper(*args):
        if args not in cache:    # При каждом вызове проверяйте, не было ли уже аналогичного вызова
            cache[args] = func(*args)
        return cache[args]
    return wrapper


def select_sorted(sort_columns=['high'], limit=30, group_by_name=False, order='desc', filename='dump.csv'):
    """Функция добавляет в список данные для поледующей сортировки ( по колонке sort_columns)"""
    with open('all.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
             if row[sort_columns[0]] != '':
                slovar.append(row[sort_columns[0]])


def partition(nums, low, high):
    """Функция быстрой сортировки"""
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)



slovar = []
cache = set()
select_sorted(sort_columns=["high"], limit=30, group_by_name=False, order='desc', filename='dump.csv')
slovar = list(map(float, slovar))
quick_sort(slovar)
cache.update(slovar)

