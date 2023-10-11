class Beverage:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def getPrice(self):
    return self.price

class VendingMachine:
  def __init__(self):
    self.beverages = {}

  def addBeverage(self, beverage):
    self.beverages[beverage.name] = beverage

  def getPrice(self, beverageName):
    if beverageName not in self.beverages:
      return -1.0
    return self.beverages[beverageName].getPrice()

vendingMachine = VendingMachine()
vendingMachine.addBeverage(Beverage("coca cola", 3200))
vendingMachine.addBeverage(Beverage("suv", 1000))
vendingMachine.addBeverage(Beverage("pepsi", 2500))

def askForDrinkPrice():
  beverageName = input("Qaysi ichimlikning narxini xohlaysiz? ")
  price = vendingMachine.getPrice(beverageName)
  if price == -1.0:
    print("Bunday ichimlik mavjud emas.")
  else:
    print(f"{beverageName} ning narxi {price}.")

askForDrinkPrice()
