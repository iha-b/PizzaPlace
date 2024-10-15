from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.toppings = []
        if size == "S":
            self.setPrice(8.00)
        elif size == "M":
            self.setPrice(10.00)
        elif size == "L":
            self.setPrice(12.00)
    def addTopping(self, topping):
        self.toppings.append(topping)
        if self.size == "S":
            self.setPrice(self.price + 0.50)
        elif self.size == "M":
            self.setPrice(self.price + 0.75)
        elif self.size == "L":
            self.setPrice(self.price + 1.00)
    def getPizzaDetails(self):
        string = "CUSTOM PIZZA\nSize: {}\nToppings:\n".format(self.size)
        if not self.toppings:
            string += ""
        else:
            for t in self.toppings:
                string +="\t+ {}\n".format(t)
        string += "Price: ${:.2f}\n".format(self.price)
        return string




