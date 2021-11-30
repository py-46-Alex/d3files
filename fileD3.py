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
    for aprove in dishes:
        dish_approve = []
        dish_approve.append(aprove)
    for each in (set(dish_approve)):
        set_reapeat = {}
        set_reapeat[each] = dishes.count(each)
    for dish1 in dishes:
        dish_approve.append(dish1)
    for dish_for_rezult in set(set_reapeat):
        rezult = {}
        for status in cook_book.get(dish_for_rezult):
            options_mesh = {}
            options_mesh['measure'] = status.get('measure')
            options_quanti = {}
            options_quanti['quantity'] = int(status.get('quantity')) * person_count * int(set_reapeat[dish_for_rezult])
            all_option = {}
            all_option = options_mesh | options_quanti
            rezult[status.get('ingredient_name')] = all_option
        pprint(rezult)

get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)
