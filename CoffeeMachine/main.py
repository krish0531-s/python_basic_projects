from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu_obj = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()



while True:
    order = input('Do u want to order? ')
    if order == 'no':
        break
    user = input('Customer/Employee: ')
    if user == 'Employee':
        operation = input('Money Report/Machine Report/Off')
        if operation == 'Money Report':
            money.report()
        elif operation == 'Machine Report': 
            coffee.report()
        elif operation == 'off':
            break

    else:
        print(menu_obj.get_items())                                     #print menu
        choice = input('Which Beverage would you like to have? ')       #get user input
        drink = menu_obj.find_drink(choice)                             #check if drink is available
        sufficient = coffee.is_resource_sufficient(drink)               #Check if resources available
        if sufficient == True:                                          #If resources are sufficent make coffee 
            for i in menu_obj.menu:                                     #Object of MenuItem Class Accessed from menu_obj object of Menu
                if i.name == choice:                                    
                    print('Cost is: ',i.cost)                           #Print Cost of chosen drink  
                    paid = money.make_payment(i.cost)
                    if paid == True:
                        coffee.make_coffee(drink)
                    





# money.report()
# coffee.report()











