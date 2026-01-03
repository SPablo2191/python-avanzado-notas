def by_reference(my_list):
    my_list.append(4)
    print("Inside function:", my_list)

def by_value(my_number):
    my_number = my_number + 1
    print("Inside function:", my_number)

original_list = [1, 2, 3]
by_reference(original_list)
print("Outside function:", original_list)

original_number = 10
by_value(original_number)
print("Outside function:", original_number) 