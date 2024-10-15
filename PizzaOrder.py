from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder:
    def __init__(self, time):
            self.pizzas = []
            self.time = time

    def getTime(self):
            return self.time

    def setTime(self, time):
        self.time = time
        
    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        string = "******\nOrder Time: {}\n".format(self.time)
        totalprice = 0.0
        for p in self.pizzas:
            string += p.getPizzaDetails() + "\n"
            totalprice += p.getPrice()
            string += "----\n"
        string += "TOTAL ORDER PRICE: ${:.2f}\n".format(totalprice)
        string += "******\n"
        return string

