import sys
from rich import print
from rich.prompt import Prompt
import tempMath
import cookMath

OFFSET_CHAR = '-'


def temp_menu():
    """Temperature conversion menu"""
    header = "Temperature Conversions Menu"
    print(header.center(50, OFFSET_CHAR))
    print("""
    1. CONVERT CELSIUS TO FAHRENHEIT
    2. CONVERT FAHRENHEIT TO CELSIUS
    3. CALCULATE DEW POINT

       """)


def currency_menu():
    header = "Currency Conversion Menu"
    print(header.center(50, OFFSET_CHAR))
    print("""
    1. CONVERT FROM USD TO DENOM OF YOUR CHOICE
    """)


def cooking_menu():
    header = "Cooking Conversion Menu"
    print(header.center(50, OFFSET_CHAR))
    print("""
    1. PRINT TABLE OF QUICK VOLUME CONVERSIONS.
    2. CONVERT GALLONS TO CUPS
    3. CONVERT CUPS TO TABLESPOONS

    8. BACK TO MAIN MENU
    9. EXIT PROGRAM

    """)
    menu_choice = Prompt.ask("Enter your choice", choices=[
                             '1', '2', '3', '8', '9'])
    if menu_choice == '1':
        cookMath.print_conv_table()


def print_main_menu():
    """Emulate a 'main' menu"""
    header = "Main Menu"
    print(header.center(50, OFFSET_CHAR))
    print("""
    1. TEMPERATURE / WEATHER
    2. CURRENCY
    3. COOKING
    
    9. EXIT PROGRAM
    """)


def menu():
    print_main_menu()
    menu_choice = 0

    while menu_choice != 9:
        menu_choice = Prompt.ask("Enter your choice", choices=[
            '1', '2', '3',  '9'
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
