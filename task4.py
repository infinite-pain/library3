while True:
    mylist = list(map(int, input('Введите более 4 чисел: ').split()))
    if len(mylist) >= 4:
        break
    else:
        print('Должно быть введено не менее 4 чисел!')

mylist.remove(min(mylist))
mylist.remove(max(mylist))

print(mylist)