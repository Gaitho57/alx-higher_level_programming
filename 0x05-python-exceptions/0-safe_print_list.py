def safe_print_list(my_list=[], x=0):
    try:
        index = 0
        for element in my_list:
            if index < x:
                print(element, end='')
                index += 1
        print()
        return index
    except:
        print()
        return index
