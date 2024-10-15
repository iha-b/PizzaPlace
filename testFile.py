from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue


def test_CustomPizza():
    cp1 = CustomPizza("L")
    cp1.addTopping("pineapple")
    cp1.addTopping("pepperoni")
    assert cp1.getPizzaDetails() == \
           "CUSTOM PIZZA\n"\
            "Size: L\n"\
            "Toppings:\n"\
            "\t+ pineapple\n"\
            "\t+ pepperoni\n"\
            "Price: $14.00\n"
    cp2 = CustomPizza("M")
    assert cp2.getPizzaDetails() == \
            "CUSTOM PIZZA\n"\
            "Size: M\n"\
            "Toppings:\n"\
            "Price: $10.00\n"

def test_SpecialtyPizza():
    sp1 = SpecialtyPizza("L", "Veggie Delight")
    assert sp1.getPizzaDetails() == \
            "SPECIALTY PIZZA\n"\
            "Size: L\n"\
            "Name: Veggie Delight\n"\
            "Price: $16.00\n"

def test_PizzaOrder():
    cp1 = CustomPizza("M")
    cp1.addTopping("olives")
    cp1.addTopping("mushrooms")
    sp1 = SpecialtyPizza("S", "Pepperoni Paradise")
    order = PizzaOrder(143000) #2:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
            "******\n"\
            "Order Time: 143000\n"\
            "CUSTOM PIZZA\n"\
            "Size: M\n"\
            "Toppings:\n"\
            "\t+ olives\n"\
            "\t+ mushrooms\n"\
            "Price: $11.50\n"\
            "\n"\
            "----\n"\
            "SPECIALTY PIZZA\n"\
            "Size: S\n"\
            "Name: Pepperoni Paradise\n"\
            "Price: $12.00\n"\
            "\n"\
            "----\n"\
            "TOTAL ORDER PRICE: $23.50\n"\
            "******\n"
   

def test_OrderQueue():
    cp1 = CustomPizza("M")
    cp1.addTopping("extra cheese")
    cp1.addTopping("pepperoni")
    sp1 = SpecialtyPizza("M", "Carne-more")
    order1 = PizzaOrder(223000) 
    order1.addPizza(cp1)
    order1.addPizza(sp1)
    sp2 = SpecialtyPizza("L", "Veggie Delight")
    order2 = PizzaOrder(120000)
    order2.addPizza(sp2)
    o = OrderQueue()
    o.addOrder(order1)
    o.addOrder(order2)

    assert o.processNextOrder() == order2.getOrderDescription()
    assert o.processNextOrder() == order1.getOrderDescription()
    assert o.process

