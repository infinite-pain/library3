n = int(input())
mas, age, sur, first, second = [], [], [], [], []

for i in range(n):
    s = input()
    mas.append(s)

for i in range(n):
    lol = mas[i].split()
    age.append(lol[1])
    sur.append(lol[0])

for i in range(n):
    if 20 <= int(age[i]) <= 40:
        k = sur[i] + ','
        second.append(k)
    else:
        k = sur[i] + ','
        first.append(k)

first.sort()
second.sort()

print('First team:', *first)
print('Second team:', *second)