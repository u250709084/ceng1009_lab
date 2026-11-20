# myList = [76, 92, 3, "hello", True, 4, 76]
#
# myList.append("apple")
# myList.append(76)
# myList.insert(3, "cat")
# myList.insert(0, 99)
# print(myList)
#
# print(myList.index("hello"))
# print(myList.count(76))
# myList.remove(76)
# print(myList)
#
# myList.pop(myList.index(True))
# print(myList)

# def sum_of_squares(number_list):
#     total =0
#     for number in number_list:
#         total = total + number**2
#     return total
#
# my_list = [3, 4, 5]
# print(sum_of_squares(my_list))

# def sum_evens(number_list):
#     sum = 0
#     for number in number_list:
#         if number % 2 == 0:
#             sum += number
#     return sum
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum_evens(my_list))

# def count_five_letters(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
#
# my_list = ["apple", "cat", "lemon", "python", "tiger"]
# print(count_five_letters(my_list))

# def sum_until_even(number_list):
#     sum = 0
#     for number in number_list:
#         if number % 2 == 0:
#             break
#         sum += number
#     return sum
#
# my_list = [1, 3, 3, 7, 5, 6]
# print(sum_until_even(my_list))

# def count_until_sam(words):
#     count = 0
#     for word in words:
#         count = count + 1
#         if word == 'sam':
#             break
#     return count
#
# my_list = ["görkem", "mehmet","kaya", "sam"]
# print(count_until_sam(my_list))

# def replace(s, old, new):
#     pieces = s.split(old)
#     return new.join(pieces)
#
# def test(actual, expected):
#     if actual == expected:
#         print("PASSED!")
#     else:
#         print("FAİLED!")
#
# test(replace("Mississippi", "i", "I"), "MIssIssIppI")

# def find_max_val_in_list(num_list):
#     max_val = num_list[0]
#     for num in num_list:
#         if num > max_val:
#             max_val = num
#     return max_val
#
# print(find_max_val_in_list([1,2,3,4,5,6,7,8,9,10]))
# print(find_max_val_in_list([-34,-35,-60,-5]))