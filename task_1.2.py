# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random
# создаем список из продолжительности каждой песни 
sound_time = [3.03, 4.02, 3.40, 5.28, 4.15, 4.04, 2.58] 

# генерируем продолжительность 3 случайных песен
print(random.sample(sound_time, 3))

# получаем три значения продолжительности песен
a = 4.15
b = 2.58
c = 3.4

# выводим на консоль сумму трех случайных песен
print('Три песни звучат ', (a + b + c), 'минут')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

import random

sound_time = [3.03, 4.02, 3.40, 5.28, 4.15, 4.04, 2.58] 

print(random.sample(sound_time, 3))

a = 4.15
b = 2.58
c = 3.4

print('Три песни звучат ', (a + b + c), 'минут')

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

import random
print(random.sample(my_favorite_songs, 3))
print(random.sample(my_favorite_songs_dict, 3))

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

import datetime
n = 2075
time_format = str(datetime.timedelta(seconds=n))
print(time_format)





