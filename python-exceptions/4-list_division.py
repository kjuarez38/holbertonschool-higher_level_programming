#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                if my_list_2[i] != 0:
                    result.append(my_list_1[i] / my_list_2[i])
                else:
                    result.append(0)
                    print("division by 0")
            else:
                result.append(0)
                print("wrong type")
        except IndexError as err:
            result.append(0)
            print(err)
        finally:
            pass
    return result
