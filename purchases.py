class PurchaseItem():
    def __init__(self, name='no item', unit_price=0):
        self._name = name
        self._unit_price = unit_price

    def getPrice(self):
        return self._unit_price

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def __str__(self):
        return f'{self._name} @ {self._unit_price}'


class WeighedItem(PurchaseItem):
    def __init__(self, name, unit_price, weight):
        super().__init__(name=name, unit_price=unit_price)
        self._weight = weight

    def getPrice(self):
        return super().getPrice() * self._weight

    def getWeight(self):
        return self._weight

    def setWeight(self, weight):
        self._weight = weight

    def __str__(self):
        return super().__str__() + f' {self._weight} kg {self.getPrice()} SR'


class CountedItem(PurchaseItem):
    def __init__(self, name, unit_price, quantity):
        super().__init__(name=name, unit_price=unit_price)
        self._quantity = quantity

    def getPrice(self):
        return super().getPrice * self._quantity

    def getQuantity(self):
        return self._quantity

    def setQuantity(self, quantity):
        self._quantity = quantity

    def __str__(self):
        return super().__str__() + f' {self._quantity} units {self.getPrice()} SR'


class SuperList(list):
    def __len__(self) -> int:
        return 1000


proceed = True

while proceed == True:
    print("1) Square \n2) Triangle")
    choice = int(input("Enter a number: "))
    if choice == 1:
        print("Ooohoo (Land of Wano sound)...you have chosen a square")
        length = float(input(
            "Enter the length of one of the sides of the square, I want to find the area"))
        print("The area of the square is: ", length**2)
    elif choice == 2:
        print("Duh..you chose a triangle")
        height = float(input("How high is the triangle? : "))
        base = float(input("How wide is the base? : "))
        print("The area of your triangle is: ", (1/2) * base * height)
    else:
        print("You've gotta learn to follow simple instructions B**CH")
    response = input('Would you like to try again? [Y/N]')
    proceed = False if response == 'N' else True
