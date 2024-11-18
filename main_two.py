"""Домашнее задание по третьему семинару"""

"""Задача №1"""

# n = int(input())
# k = 0
# for i in range(n):
#     v = int(input())
#     if v == 1:
#         k += 1
# print(k if k < n / 2 else n - k)

"""Задача №2"""

a, b = map(int, input().split())
res = []
for i in range(a + b):
    if i == (a * i - b)** 0.5:
        res.append(i)
print(*res if len(res) == 2 else res + res)        