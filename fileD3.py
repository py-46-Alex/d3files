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

def get_shop_list_by_dishes(dishes, person_count):
    for dish1 in dishes:
        rezult = {}
        if dish1 in cook_book.keys():
            for status in cook_book.get(dish1):
                options_mesh = {}
                options_mesh['measure'] = status.get('measure')
                options_quanti = {}
                options_quanti['quantity'] = int(status.get('quantity')) * person_count
                all_option = {}
                all_option = options_mesh | options_quanti
                rezult[status.get('ingredient_name')] = all_option
        pprint(rezult)

get_shop_list_by_dishes(['Омлет','Омлет','Фахитос'], 1)
