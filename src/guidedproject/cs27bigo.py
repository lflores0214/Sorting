import random
import time
from datetime import datetime

# my_range = 10
# my_size = 10

# my_random = random.sample(range(my_range), my_size)

# print(my_random)


# def print_number(n):
#     print(my_random[n])


# print_number(4)

# def print_array(arr):
#     for i in range(len(arr)):
#         print(arr[i])
# print_array(my_random)


# animals = ['Duck',
#            'Jackal',
#            'Hippo',
#            'Aardvark',
#            'Cat',
#            'Flamingo',
#            'Iguana',
#            'Giraffe',
#            'Elephant',
#            'Bear',
#            ]

# def print_animals(animal_list):
#     my_number = 0
#     for i in range(len(animal_list)):
#         print(animal_list[i])


# # print_animals(animals)

# my_range = 10
# my_size = 10

# my_random = random.sample(range(my_range), my_size)

# # print(my_random)

# searching_for = 7


# def find_in_number():
#     for i in range(len(my_random)):
#         if my_random[i] == seraching_for:
#             return True
#     return False


# def find_value_binary(arr, value):
#     if len(arr) <= 0:
#         # TODO handle edge
#         pass
#     first = 0
#     last = (len(arr) - 1)
#     found = False
#     while first <= last and not found:
#         # find middle using integer division
#         middle = (first + last) // 2

#         if arr[middle] == value:
#             found = True
#         else:
#             if value < arr[middle]:
#                 # search upper half
#                 last = middle - 1
#             else:
#                 # search upper half of remainder
#                 first - middle + 1
#     return found

# print("binary")
# start = datetime.now()
# my_random.sort()
# print(find_value_binary(my_random, searching_for))
# end = datetime.now()
# print(f"Runtime: {end - start}")


my_list = [8, 2, 5, 4, 1, 3]


def insertion_sort(list_to_sort):
    # separate first element, think of it as sorted

    # for all other indices, start at 1
    for i in range(1, len(list_to_sort)):
        # put current number in a temp variable
        temp = list_to_sort[i]
        # look left, until we find where it belongs
        j = i
        while j > 0 and temp < list_to_sort[j - 1]:
            print(j)
        # as we look left, shift items to the right as we iterate
            list_to_sort[j] = list_to_sort[j-1]
            j -= 1
        # when left is smaller than temp, or we're at zero, put temp at this spot
        list_to_sort[j] = temp
    return list_to_sort
print(insertion_sort(my_list))