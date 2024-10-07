#*******************************************************************************************************************
#Coffee Machine in OOP
#Carlos Cartagena
#10/7/2024
#The purpose of this program is to take previous project of named "Coffee Machine" and -
#code it in OOP.
#*******************************************************************************************************************
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#making new variables
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


flag = True

while flag:
    options = menu.get_items()
    user_input = input(f"What would you like? {options}: ").lower()   
    if user_input == "off":
        flag = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
         drink = menu.find_drink(user_input)
         if coffee_maker.is_resource_sufficient(drink) and  money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        
         
         
         