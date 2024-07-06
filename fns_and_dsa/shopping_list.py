shopping_list = []
def functionality(add_item, remove_item, view_list, exit):
    if add_item:
        shopping_list.append()
    elif remove_item:
        shopping_list.remove()
    elif view_list:
        for items in shopping_list:
            print(items)
    elif exit:
        print()
functionality("1","2","3","4")