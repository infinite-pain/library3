numbers = [432, 43233, 564093390, 238, 47388]
x_min = min(numbers)
x_max = max(numbers)

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] *= x_min
    else:
        numbers[i] *= x_max

print(numbers)