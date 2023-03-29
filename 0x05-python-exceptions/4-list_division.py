#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        for j in range(list_length):
            result = 0
            try:
                result = my_list_1[i] / my_list_2[j]
            except TypeError:
                print("wrong type")
                continue
            except ZeroDivisionError:
                print("division by 0")
            except IndexError:
                print("out of range")
            finally:
                new_list.append(result)
    return new_list
