# Задача 1:

cook_book = {}

def food_list():
    with open('recipes.txt', 'r', encoding='utf8') as recipes:
        for line in recipes:
            food_name = line.strip()
            cook_book[food_name] = []
            products_count = recipes.readline()
            for i in range(int(products_count)):
                prod = recipes.readline()
                ingredient_name, quantity, measure = prod.split(' | ')
                recipe = {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()}
                cook_book[food_name].append(recipe)
            recipes.readline()
    return

# Задача 2

def get_shop_list_by_dishes(dishes = None, person_count = int):
    if dishes is None:
        dishes = []
    dishes_list = dishes
    for foods in dishes_list:
        food = cook_book[foods]
        for list in food:
            ingredient_name = list.get('ingredient_name')
            quantity = list.get('quantity')
            measure = list.get('measure')
            my_dict = {ingredient_name:{'measure': measure, 'quantity': quantity * person_count}}
    return

food_list()
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 2)

# Задача 3

import os

text_list = []

def open_file():
    with open('1.txt', 'r', encoding='utf8') as first:
        first_one = first.readlines()
        first_one = [line.strip() for line in first_one]
        text_first_one_name = os.path.basename(r"C:\Users\79265\OneDrive\Рабочий стол\Учеба\Прогинг\Netology\Открытие и чтение файла, запись в файл\Дз\1.txt")
        text_first_one = [len(first_one), text_first_one_name, first_one]
        text_list.append(text_first_one)
    with open('2.txt', 'r', encoding='utf8') as secound:
        secound_one = secound.readlines()
        secound_one = [line.strip() for line in secound_one]
        text_secound_one_name = os.path.basename(r"C:\Users\79265\OneDrive\Рабочий стол\Учеба\Прогинг\Netology\Открытие и чтение файла, запись в файл\Дз\2.txt")
        text_secound_one = [len(secound_one), text_secound_one_name, secound_one]
        text_list.append(text_secound_one)
    with open('3.txt', 'r', encoding='utf8') as third:
        third_one = third.readlines()
        third_one = [line.strip() for line in third_one]
        text_third_one_name = os.path.basename(r"C:\Users\79265\OneDrive\Рабочий стол\Учеба\Прогинг\Netology\Открытие и чтение файла, запись в файл\Дз\3.txt")
        text_third_one = [len(third_one), text_third_one_name, third_one]
        text_list.append(text_third_one)
    text_list.sort()
    with open('final.txt', 'w', encoding='utf8') as final_file:
        for i in text_list:
            i2 = '\n'.join(i[2])
            final_file.write(f'{i[1]}\n{i[0]}\n{i2}\n')
    return

open_file()
