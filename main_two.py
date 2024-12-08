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

# from random import randint
# n_set = set(randint(1, 20) for i in range(int(input())))
# print(n_set)
# m_set = set(randint(1, 20) for i in range(int(input())))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)


"""Задача №2"""

# n = int(input())
# k = [int(x) for x in input().split()]
# n = len(k)
# k = k + k[:2]
# ma = 0
# for i in range(n):
#     ma = max(ma, k[i] + k[i+1] + k[i+2])
# print(ma)

"""Домашнее задание по пятому семинару"""


"""Задача #1"""

# def recAB(a, b):
#     if b == 0:
#         return 1
#     return a * recAB(a, b - 1)

# a = int(input())
# b = int(input())

# print(recAB(a, b))


"""Задача №2"""


# def sum(a, b):
#     if b == 0:
#         return a
#     else:
#         if b > 0:
#             return sum(a + 1, b - 1)
#         else:
#             return sum(a - 1, b + 1)

# print(sum(int(input()), int(input())))


"""Домашнее задание по шестому семинару"""


"""Задача #1"""


# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#     print(a1 + i * d, end=' ')


"""Задача №2"""


# list=[-5,9,0,3,-1,-2,1,4,-2,10,2,0,-9,8,10,-9,0,-5,-5,7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list)):
#     if min_number <= list[i] <= max_number:
#         print(i)



"""Домашнее задание по седьмому семинару"""


"""Задача #1"""


# def ritm(chant):
#     st = chant.lower().split()
#     f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
#     tmp = f(st[0])
#     if all([f(i) == tmp for i in st]):
#         return 'Парам пам-пам'
#     return 'Пам парам'
 
# print(ritm("пара-ра-рам рам-пам-папам па-ра-па-дам"))


"""Задача №2"""


# def print_operation_table(operation, num_rows, num_сolumns):
#     arr=[[operation(i,j) for i in range(1,num_rows+1)] for j in range(1, num_сolumns + 1)]
#     for i in arr:
#         print(*[f"{x:>3}"for x in i])
# line = int(input())
# columns = int(input())
# print_operation_table(lambda x, y: x * y, line, columns)