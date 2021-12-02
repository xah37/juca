from rich.prompt import Prompt
from rich import print
import sys

# Custom
import tabular


def print_main_menu():
    """Emulate a 'main' menu"""
    header = "Main Menu"
    print(header.center(50, '-'))
    print("""
    1. TEMPERATURE / WEATHER
    2. CURRENCY
    3. COOKING

    9. EXIT PROGRAM
    """)


def temp_menu():
    """Temperature conversion menu"""
    header = "Temperature Conversions Menu"
    print(header.center(50, '-'))
    print("""
    1. CONVERT CELSIUS TO FAHRENHEIT
    2. CONVERT FAHRENHEIT TO CELSIUS
    3. CALCULATE DEW POINT

    8. BACK TO MAIN MENU
    9. EXIT PROGRAM
""")
    menu_choice = Prompt.ask("Enter your choice", choices=[
                             '1', '2', '3', '8', '9'])
    while True:
        if menu_choice == '1':
            i = int(
                input('Enter the temperature in celsius to convert to fahrenheit: '))
            print(f"{i} * celsius is equivalent to {(i * 9/5) + 32} fahrenheit. ")
        elif menu_choice == '2':
            i = int(
                input('Enter the temperature in fahrenheit to convert to celsius '))
            print(f"{i} * fahrenheit is equivalent to {(i-32) * 5/9} celsius.")
        elif menu_choice == '3':
            i = int(input('Enter the amount of cups to convert to tablespoons '))
            print(f"{i} cups is equivalent to {i*16} tablespoons")
        elif menu_choice == '8':
            print_main_menu()
        elif menu_choice == '9':
            print('Quitting!')
            sys.exit()


def currency_menu():
    header = "Currency Conversion Menu"
    print(header.center(50, '-'))
    print("""
    1. CONVERT FROM USD TO DENOM OF YOUR CHOICE
""")


def cooking_menu():
    header = "Cooking Conversion Menu"
    print(header.center(50, '-'))
    print("""
    1. PRINT TABLE OF QUICK VOLUME CONVERSIONS.
    2. CONVERT GALLONS TO CUPS
    3. CONVERT CUPS TO TABLESPOONS

    8. BACK TO MAIN MENU
    9. EXIT PROGRAM

    """)

    menu_choice = Prompt.ask("Enter your choice", choices=[
                             '1', '2', '3', '8', '9'])

    while True:
        if menu_choice == '1':
            tabular.print_conv_table()
        elif menu_choice == '2':
            i = int(input('Enter the amount of gallons to convert to cups '))
            print(f"{i} gallons is equivalent to {i*16} cups.")
        elif menu_choice == '3':
            i = int(input('Enter the amount of cups to convert to tablespoons '))
            print(f"{i} cups is equivalent to {i*16} tablespoons")
        elif menu_choice == '8':
            print_main_menu()
        elif menu_choice == '9':
            print('Quitting!')
            sys.exit()


def menu():
    print_main_menu()
    menu_choice = 0

    while True:
        menu_choice = Prompt.ask("Enter your choice", choices=['1', '2', '3', '9'
                                                               ])

        if menu_choice == '1':
            temp_menu()
            break
        elif menu_choice == '2':
            currency_menu()
            break
        elif menu_choice == '3':
            cooking_menu()
            break
        elif menu_choice == '4':
            pass
        elif menu_choice == '9':
            print('Exiting')
            sys.exit()
