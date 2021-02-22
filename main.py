todayPizzas = []
print("Welcome!")
pizzas_to_bake = int(input("How many pizzas can we bake today: "))
print(todayPizzas.append(pizzas_to_bake))

class Pizza:

    def __init__(self,size_of_pizza,cheese_toppings, pepperoni_toppings,mushroom_toppings):
        self.size_of_pizza = size_of_pizza
        self.cheese_toppings = cheese_toppings
        self.pepperoni_toppings = pepperoni_toppings
        self.mushroom_toppings = mushroom_toppings
    def set_size_of_pizza(self):
        value = input("Enter the size of pizza 1.small 2.medium 3. large: ")
        convert_value = value.lower()
        self.size_of_pizza = convert_value



    def set_cheese_toppings(self):
        value = int(input("Enter the number of cheese_toppings: "))

    def set_pepperoni_toppings(self):
        value = int(input("Enter the number of pepperoni toppings: "))
        self.pepperoni_toppings = value

    def set_mushroom_toppings(self):
        value = int(input("Enter the number of mushroom toppings: "))
        self.mushroom_toppings = value

    def get_size_of_pizza(self):
        return self.size_of_pizza

    def get_cheese_toppings(self):
        return self.cheese_toppings

    def get_pepperoni_toppings(self):
        return self.pepperoni_toppings

    def get_mushroom_toppings(self):
        return self.mushroom_toppings


    def calCost(self):

        if self.size_of_pizza == 'small':
            total_cost = 10 + ((self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings)*2)

        elif self.size_of_pizza == 'medium':
            total_cost = 12 +((self.cheese_toppings + self.pepperoni_toppings + self.pepperoni_toppings)*2)

        elif self.size_of_pizza == 'large':
            total_cost = 14 + ((self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings)*2)

        else:
            print("You have entered invalid size of pizza.")
        return total_cost

    def __str__(self):
        cost = object.calCost()
        return f'The total cost is : {cost}$'

class DeluxPizza(Pizza):
    number_of_pizzas = 0
    def __init__(self,size_of_pizza,cheese_toppings, pepperoni_toppings,mushroom_toppings,stuffed_cheese, veggie_toppings):
        Pizza.__init__(self,size_of_pizza,cheese_toppings,pepperoni_toppings,mushroom_toppings)
        self.stuffed_cheese = stuffed_cheese
        self.veggie_toppings = veggie_toppings
        DeluxPizza.number_of_pizzas += 1

    def set_stuffed_cheese(self):
        value = int(input('Do you want pizza with stuffed cheese: '))
        self.stuffed_cheese = value
    def set_veggie_toppings(self):
        value = int(input("Enter the number of veggie toppings: "))
        self.veggie_toppings = value
    def get_stuffed_cheese(self):
        return self.stuffed_cheese
    def get_veggie_toppings(self):
        return self.veggie_toppings
    def set_number_of_pizzas(self,number_of_pizzas):
        self.number_of_pizzas = number_of_pizzas
    def calCost(self):
            total_cost = 0
            if self.size_of_pizza == 'small':
                total_cost = 10 + ((self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings)*2 + (self.veggie_toppings*3))
                if self.stuffed_cheese == True:
                    total_cost += 2
            elif self.size_of_pizza == 'medium':
                total_cost = 12 +((self.cheese_toppings + self.pepperoni_toppings + self.pepperoni_toppings)*2 + (self.veggie_toppings*3))
                if self.stuffed_cheese == True:
                    total_cost += 4
            elif self.size_of_pizza == 'large':
                total_cost = 14 + ((self.cheese_toppings + self.pepperoni_toppings + self.mushroom_toppings)*2 ++ (self.veggie_toppings*3))
                if self.stuffed_cheese == True:
                    total_cost += 6


            return total_cost

    def __str__(self):
        cost = object.calCost()
        output = f"Pizza size:{self.size_of_pizza}\n" \
               f"Cheese filled dough:{bool(self.stuffed_cheese)}\n" \
               f"Number of Cheese toppings:{self.cheese_toppings}\n" \
               f"Number of pepperoni toppings:{self.pepperoni_toppings}\n" \
               f"Number of mushroom toppings:{self.mushroom_toppings}\n" \
               f"Number of vegetable toppings:{self.veggie_toppings}\n" \
                 f"Price:{cost}$"
        return output



object = DeluxPizza('',0,0,0,0,0)
object.set_size_of_pizza()
object.get_size_of_pizza()
object.set_cheese_toppings()
object.get_cheese_toppings()
object.set_pepperoni_toppings()
object.get_pepperoni_toppings()
object.set_mushroom_toppings()
object.get_mushroom_toppings()
object.set_stuffed_cheese()
object.get_stuffed_cheese()
object.set_veggie_toppings()
object.get_veggie_toppings()
object.calCost()
print(object.__str__())