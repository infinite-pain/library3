class House():
    """описание дома"""
    def __init__(self, street, number):
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        """Строит дом"""
        print("Дом на улице " + self.street + " под номером " + str(self.number) + " построен.")

    def age_of_house(self, year):
        """Возраст дома"""
        self.age += year

House1 = House("Московская", 20)
House2 = House("Крупской", 48)

House1.age_of_house(5)
print(House1.age)