import os
def book_to_dict(path):
    cook_book = {}
    with open(path, encoding='utf-8') as f:
        reciept = {}
        name_reciept = ''
        ingridients_reciept = []
        for row in f.readlines():
            row = row.strip()
            if len(row) == 1:
                continue

            if not "|" in row:
                name_reciept = row.strip()

            if "|" in row:
                list_ingridients = row.split('|')
                ingredient_name = list_ingridients[0].strip()
                quantity = list_ingridients[1].strip()
                measure = list_ingridients[2].strip()
                ingridients_reciept.append({"ingredient_name": ingredient_name, "quantity":quantity, "measure":measure})
                cook_book[f"{name_reciept}"] = ingridients_reciept

            if len(row) == 0:
                reciept = {}
                ingridients_reciept = []

    return cook_book



def get_shop_list_by_dishes(dish_list, count_person):
    ingridient_dict = {}
    cook_book = book_to_dict('recipes.txt')
    for dish in dish_list:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                if not ingridient["ingredient_name"] in ingridient_dict:
                    new_count_ingridient = int(ingridient['quantity']) * int(count_person)
                    ingridient_dict[ingridient["ingredient_name"]] = {'measure': ingridient['measure'], 'quantity': new_count_ingridient}
                if ingridient["ingredient_name"] in ingridient_dict:
                    ingridient_dict[ingridient["ingredient_name"]]['quantity'] += int(ingridient["quantity"]) * count_person

    return ingridient_dict


# print(book_to_dict('recipes.txt'))
# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 1))

def sort_text(foler_path, result):
    list_files = os.listdir(foler_path)
    file_lenght = {}
    for file in list_files:
        with open(f'sorted/{file}', 'r', encoding='utf-8') as f:
            len_string = len(f.readlines())
            file_lenght[file] = len_string
    sorted_file_lenght = dict(sorted(file_lenght.items(), key=lambda item: item[1]))
    print(sorted_file_lenght)
    with open(f'{result}.txt', 'a', encoding='utf-8') as file_write:
        for file in sorted_file_lenght.items():
            file_write.write(f"{str(file[0])}\n{str(file[1])}\n")
            write_text = open(f"sorted/{file[0]}", 'r', encoding='utf-8')
            file_write.write(f"{write_text.read()}\n")
            write_text.close()

    # print(file_lenght)
        # with open(f'sorted/result.txt', mode='a') as write_file:
        #     with open(f'sorted/{file}', 'r', encoding='utf-8') as f:
        #         for line

sort_text('sorted', 'result')