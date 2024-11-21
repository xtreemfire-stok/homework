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

n = int(input())
list_1 = list()
for i in range(n):
    x = int(input())
    list_1.append(x)

k = int(input())
m = abs(k - list_1[0]) 

number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
