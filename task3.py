import random

n, n_min, n_max = int(input()), float(input()), float(input())
k = 0
mas = []
for i in range(n):
    mas.append(random.uniform(-10, 10))

print(mas)

for i in range(n):
    if n_min <= mas[i] <= n_max:
        k += 1

print(k)