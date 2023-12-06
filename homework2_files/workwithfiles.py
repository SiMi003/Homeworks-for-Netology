def openread(name):
    standart_descr = ['ingredient_name', 'quantity', 'measure']
    dict_ = {}
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            key_ = file.readline().strip()  # reading the first line: is a key for the dict
            if key_ == '':
                break
            numbers = int(file.readline())  # reading the number of ingredients N = the number of dicts in the list
            dict_[key_] = []  # Initialize an empty list for the key

            for _ in range(numbers):
                ingred, quant, meas = file.readline().strip().split(' | ', 2)
                ingredient_dict = {'ingredient_name': ingred, 'quantity': quant, 'measure': meas}
                dict_[key_].append(ingredient_dict)

            file.readline()  # here should be one empty line

    return dict_   

menu_main = openread('main dishes recipes.txt')
menu_sweets = openread('recipes of sweets.txt')

# Combining all dictionaries into one menu
menu_full = {**menu_main, **menu_sweets}

# View all menu variants 
import pprint
print('MAIN MENU:')
pprint.pprint(menu_main)
print('MENU OF SWEETS:')
pprint.pprint(menu_sweets)
print('FULL MENU:')
pprint.pprint(menu_full)


# We need to write a function that accepts a list of dishes from "menu_full" 
# and the number of people for whom we will cook
def get_shop_list_by_dishes(dishes, person_count):
    dict_ = {}
    list_ = []
    for dishe in dishes:
        for ingridient in menu_full[dishe]:
           key_ = ingridient['ingredient_name']
           meas = ingridient['measure']
           quant = int(ingridient['quantity'])
           if key_ in list_:
               list_[list_.index(key_)+2] += quant
           else:
               list_.extend([key_, meas, quant])
    # Multiplication by the number of persons "person_count"
    for i in range(0, len(list_), 3):
        dict_[list_[i+0]] = {'measure': list_[i+1], 'quantity': list_[i+2]*person_count}
    return dict_


# At the exit, we should get a dictionary with the name of the ingredients 
# and its quantity for the dish. 
first_order = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет','Шарлотка'], 2)
second_order = get_shop_list_by_dishes(['Вишневые вареники'], 6)

# View ingredients for all orders
import pprint
print('THE FIRST ORDER:')
pprint.pprint(first_order)
print('THE SECOND ORDER:')
pprint.pprint(second_order)