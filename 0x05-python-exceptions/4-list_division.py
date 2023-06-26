#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for idx in range(list_length):
        try:
            div = 0
            if idx < len(my_list_1) and idx < len(my_list_2):
                if isinstance(my_list_1[idx], (int, float)) and isinstance(my_list_2[idx], (int, float)):
                    if my_list_2[idx] != 0:
                        div = my_list_1[idx] / my_list_2[idx]
                    else:
                        print("division by 0")
                else:
                    print("wrong type")
            elif idx >= len(my_list_1) or idx >= len(my_list_2):
                print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            result.append(div)
    return result
