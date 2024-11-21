"""Домашнее задание по второму семинару"""

"""Задача №1"""

# n = int(input())
# k = 0
# for i in range(n):
#     v = int(input())
#     if v == 1:
#         k += 1
# print(k if k < n / 2 else n - k)

"""Задача №2"""

# a, b = map(int, input().split())
# res = []
# for i in range(a + b):
#     if i == (a * i - b)** 0.5:
#         res.append(i)
# print(*res if len(res) == 2 else res + res)

"""Здача #3"""

# n = int(input())
# k = 0
# while 2**k <= n:
#     print(2**k, end=" ")
#     k += 1
# print()


"""Домашнее задание по третьему семинару"""

"""Задача #1"""

# import random
# n = int(input())
# x = int(input())
# n_array = [1, 2, 3, 4, 5]
# for i in range(n):
#     n_array.append(random.randint(0, n//2))
# print(f' count {n_array.count(x)}')


"""Задача №2"""

# n = int(input())
# list_1 = list()
# for i in range(n):
#     x = int(input())
#     list_1.append(x)

# k = int(input())
# m = abs(k - list_1[0]) 

# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)


"""Здача #3"""

# dict_with_letter = {1: ("А","Е","В","И","Н","О","Р","С","Т", 
#  'A','E','I','O','U','L','N','S','T','R'), 
#  2: ("Д","К","Л","М","П","У", 
#  'D', 'G'), 
#  3: ("Б","Г","Ё","Ь","Я", 
#  'B','C','M', 'P'), 
#  4: ("Й","Ы", 
#  'F', 'H', 'V', 'W', 'Y'), 
#  5: ("Ж","З","Х","Ц","Ч", 
#  'K'), 
#  6: ("Ш", "Э","Ю", 
#  'J','X'), 
#  7: ("Ф","Щ","Ъ", 
#  'Q','Z') 
#  } 
 
# def dicting(dict_with, words): 
#  sum_points = 0 
#  for key, value in dict_with.items(): 
#   for letter in words.upper(): 
#    if letter in value: 
#     sum_points += key 
#  print(sum_points) 
# word = str(input()) 
# dicting(dict_with_letter,word)


"""Домашнее задание по четвертому семинару"""

"""Задача #1"""

from random import randint
n_set = set(randint(1, 20) for i in range(int(input())))
print(n_set)
m_set = set(randint(1, 20) for i in range(int(input())))
print(m_set)
s_set = sorted(n_set.intersection(m_set))
print(*s_set)