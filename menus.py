from rich.prompt import Prompt
from rich import print
import sys

# Custom
import tabular


def cookingMenu():
    # Initial value for variable other than 'quit'
    menu_choice = ''

    # Start menu loop
    while menu_choice != 'q':
        header = "Cooking Conversion Menu"
        print(header.center(50, '-'))
        print('\n:cooking: [1] Display Table of Quick Volume Conversions.')
        print(":cooking: [2] Convert gallons to cups.")
        print(":cooking: [3] Convert cups to tablespoons.")
        print("")
        print(f":back:\\[b] Return to the Main Menu")
        print(f":stop_sign:\\[q] Exit the program.")

        # Get users choice
        menu_choice = Prompt.ask("Enter your choice", choices=[
            '1', '2', '3', 'b', 'q', ])

        if menu_choice == '1':
            pass
        elif menu_choice == '2':
            pass
        elif menu_choice == '3':
            pass
        elif menu_choice == 'b':
            pass
        elif menu_choice == 'q':
            print('exiting')
            sys.exit()
        else:
            print("You've broken me.")


def temperatureMenu():
   # Initial value for variable other than 'quit'
    menu_choice = ''

    # Start menu loop
    while menu_choice != 'q':
        header = "Temperature Conversion Menu"
        print(header.center(50, '-'))
        print('\n:thermometer: [1] Convert Celsius to Fahrenheit.')
        print(":thermometer: [2] Convert Fahrenheit to Celsius.")
        print(":thermometer: [3] Calculate the Dew Point.")
        print("")
        print(f":back:\\[b] Return to the Main Menu")
        print(f":stop_sign:\\[q] Exit the program.")

        # Get users choice
        menu_choice = Prompt.ask("Enter your choice", choices=[
            '1', '2', '3', 'b', 'q', ])

        if menu_choice == '1':
            pass
        elif menu_choice == '2':
            pass
        elif menu_choice == '3':
            pass
        elif menu_choice == 'b':
            pass
        elif menu_choice == 'q':
            print('exiting')
            sys.exit()
        else:
            print("You've broken me.")


def currencyMenu():
    # Initial value for variable other than 'quit'
    menu_choice = ''

    # Start menu loop
    while menu_choice != 'q':
        header = "Currency Conversion Menu"
        print(header.center(50, '-'))
        print('\n:moneybag: [1] From USD to GBP.')
        print(":moneybag: [2] Calculate the Dew Point.")
        print("")
        print(f":back:\\[b] Return to the Main Menu")
        print(f":stop_sign:\\[q] Exit the program.")

        # Get users choice
        menu_choice = Prompt.ask("Enter your choice", choices=[
            '1', '2', '3', 'b', 'q', ])

        if menu_choice == '1':
            pass
        elif menu_choice == '2':
            pass
        elif menu_choice == '3':
            pass
        elif menu_choice == 'b':
            pass
        elif menu_choice == 'q':
            print('exiting')
            sys.exit()
        else:
            print("You've broken me.")


def mainMenu():
   # Initial value for variable other than 'quit'
    menu_choice = ''

    # Start menu loop
    while menu_choice != 'q':
        header = "Main Menu"
        print(header.center(50, '-'))
        print('\n:thermometer: [1] Temperature / Weather-related conversions.')
        print(":moneybag: [2] Currency-related conversions")
        print(":cooking: [3] Cooking-related conversions.")
        print("")
        print(f":back:\\[b] Return to the Main Menu")
        print(f":stop_sign:\\[q] Exit the program.")

        # Get users choice
        menu_choice = Prompt.ask("Enter your choice", choices=[
            '1', '2', '3', 'b', 'q', ])

        if menu_choice == '1':
            pass
        elif menu_choice == '2':
            pass
        elif menu_choice == '3':
            pass
        elif menu_choice == 'b':
            pass
        elif menu_choice == 'q':
            print('exiting')
            sys.exit()
        else:
            print("You've broken me.")
