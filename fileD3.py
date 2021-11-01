import os
from pprint import pprint

with open('recept.txt', encoding='utf-8') as fale:
    cook_book = {}
    for dinner in fale:
        dish_name = dinner.strip()
        counter = int(fale.readline().strip())
        cook_box = []
        for ingr in range(counter):
            ingredient_name, quantity, measure = fale.readline().split('|')
            cook_box.append({'ingredient_name':ingredient_name.strip(), 'quantity':int(quantity.strip()), 'measure':measure.strip()})
        cook_book[dish_name] = cook_box
        fale.readline()
print(type(cook_book))
#
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
#
def get_shop_list_by_dishes(dishes, person_count):
    person_count = float(person_count)
    if dishes in cook_book.keys():
        print(cook_book.get(dishes))
        print(f'ETO cifra {person_count}')

get_shop_list_by_dishes('Фахитос' , 11)

