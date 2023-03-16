#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in range(len(my_list)-1):
        if my_list[i] == search:
            my_list[i] = replace        
my_list = [1,2,3,4,5,6] 
print(my_list)
search_replace(my_list, 3, 10)
print(my_list)
