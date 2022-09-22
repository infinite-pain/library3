students = {
    "ibm733" : ["Ivanov"],
    "ibm732" : ["Vasileva", "Sidorov"],
    "ibm731" : ["Petrov", "Lycev"]
}

std = input()

for grp in students:
    if std in students[grp]:
        print(grp)
        break

else:
    print("студент не найден")