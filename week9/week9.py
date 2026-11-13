# def is_odd(n):
#     return n % 2 == 1
#
# print(is_odd(647))

# def is_leapyear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
#
# print(is_leapyear(2007))

# def print_triangular_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#         print(i, total)
#
# print(print_triangular_numbers(5))

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# print(is_prime(163))

# def reverse(s):
#     result = ""
#     for ch in s:
#         result = ch + result
#     return result
#
# print(reverse("Hello World"))
#
# def reverse_slice(s):
#     return s[::-1]
#
# print(reverse_slice("Hello World"))

# def remove(sub, s):
#     return s.replace(sub, " ")
#
# print(remove("ll", "Hello World"))

# def substitute(message, key):
#     alphabet = "abcçdefgğhıijklmnoöpqrsştuüvxwyz"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "qtggörkemmehmetkayaovikingschamp"
# print(substitute("QRSŞTUÜ VXWYZ", key))

def remove_dups(s):
    result = ""
    for ch in s:
        if ch.lower() not in result.lower():
            result = result + ch
    return result

    print(remove_dups("Hello World"))