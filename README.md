# Pizza Order Management System

This project implements a pizza order management system using Python. The system includes customizable pizzas, specialty pizzas, and an order queue to manage multiple orders based on their expected pickup time. The project follows object-oriented programming principles, with clear class hierarchies and pytest tests.

## Features

### 1. **Pizza (Base Class)**
   - Represents the common attributes of all pizzas.
   - **Attributes**:
     - `size`: Size of the pizza (`S`, `M`, `L`).
     - `price`: Initial price (starts at `0.0`).
   - **Methods**:
     - `getPrice()`, `setPrice()`: Access and modify price.
     - `getSize()`, `setSize()`: Access and modify size.

### 2. **CustomPizza (Inherits from Pizza)**
   - Allows customers to add their own toppings.
   - **Attributes**:
     - `toppings`: A list of toppings.
   - **Pricing**:
     - Base price determined by pizza size.
     - Additional charge per topping.
   - **Methods**:
     - `addTopping(topping)`: Adds a topping and updates the price.
     - `getPizzaDetails()`: Returns a formatted string with the pizza's size, toppings, and price.

### 3. **SpecialtyPizza (Inherits from Pizza)**
   - Pre-configured pizzas with a fixed price based on size.
   - **Attributes**:
     - `name`: Name of the specialty pizza.
   - **Methods**:
     - `getPizzaDetails()`: Returns a formatted string with the pizza's size, name, and price.

### 4. **PizzaOrder**
   - Represents a collection of pizzas ordered by a customer.
   - **Attributes**:
     - `pizzas`: A list of Pizza objects (Custom or Specialty).
     - `time`: Expected time of pickup (24-hour format).
   - **Methods**:
     - `addPizza(pizza)`: Adds a Pizza object to the order.
     - `getOrderDescription()`: Constructs a detailed description of the order, including individual pizza details and total price.

### 5. **OrderQueue (MinHeap-based Priority Queue)**
   - Manages pizza orders based on expected pickup time.
   - **Attributes**:
     - `heap`: A MinHeap storing PizzaOrder objects.
   - **Methods**:
     - `addOrder(pizzaOrder)`: Adds an order to the queue based on its time.
     - `processNextOrder()`: Processes and removes the order with the earliest pickup time.
   - **Exception**: `QueueEmptyException` is raised when trying to process an empty queue.

## Tests
Unit tests are provided in `testFile.py` using `pytest` to ensure the correctness of all class implementations.
