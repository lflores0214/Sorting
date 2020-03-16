import random
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

# animals.sort()
# print(animals)

# # * O(1)
# # * Constant

# print(animals[3])

# animals.append("Snake")

# * O(N)
# * Linear
# for i in range(0, len(animals)):
#     print(animals[i])

# print a list of every possible pair of animals in two lists
# O(n^2)
# for i in range(0, len(animals)):
#     for j in range(0, len(animals)):
#         print(animals[i] + " -- " + animals[j])

# n^3
# sum = 0
# for i in range(0, len(animals)):
#     for j in range(0, len(animals)):
#         for k in range(0, len(animals)):
#             sum += 1
#             print(animals[i] + "-" + animals[j] + "-" + animals[k])
# print(sum)
# my_range = 10000000
# size = 10000000
# my_randoms = random.sample(range(my_range), size)

# # print(my_randoms)


# my_value = random.randint(0, 10)

# * Linear
# def find_value_linear(sort_list, value):
#     for i in range(len(sort_list)):
#         if sort_list[i] == my_value:
#             return True
#         else:
#             return False


# print(find_value_linear(my_randoms, my_value))

# * binary sort
#****** must be sorted for this to work *******#

# my_randoms.sort()

# def find_value_binary(sort_list, value):
#     # edge case
#     if len(sort_list) == 0:
#         return False
#     first = 0

#     last = (len(sort_list)-1)

#     found = False

#     # loop until found or checked everything
#     while first <= last and not found:
#         # find the middle of the list using integer division
#         middle = (first + last) // 2

#         # if found update found
#         if sort_list[middle] == value:
#             found = True
#         else:
#             if value < sort_list[middle]:
#                 last = middle - 1
#             else:
#                 # search upper half of remainder
#                 first = middle + 1
#         return found


# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))
# print(find_value_binary(my_randoms, my_value))

# * insertion sort


# * original array -> [8,     2, 5, 4, 1, 3]
#        sorted  |  non-sorted
# step 1 [2, 8,   5, 4, 1, 3]
# step 2[2, 5, 8,   4, 1, 3]
# step 3[2, 4, 5, 8,   1, 3]
# step 4[1, 2, 4, 5, 8,   3]

# * final sorted array -> [1, 2, 3, 4, 5, 8]


my_list = [8, 2, 5, 4, 1, 3]


def insertion_sort(list_to_sort):
    # Separate the first element from the rest of the array. Think about it as a sorted list of one element

    # For all other indices, beginning with [1]:
    for i in range(1, len(list_to_sort)):
        # a. copy the item at that index into a temp varaiable
        temp = list_to_sort[i]
        # b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted
        j = i
        while j > 0 and temp < list_to_sort[j-1]:

            # shift items over to the right as you iterate
            list_to_sort[j] = list_to_sort[j-1]
            j -= 1
    # c. When the correct index is found copy the temp variable into this position
        list_to_sort[j] = temp

    return list_to_sort


print(insertion_sort(my_list))
