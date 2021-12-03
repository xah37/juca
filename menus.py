from rich import prompt
from rich.prompt import Prompt
from rich import print
import sys

# My fancy new Temperature class
from conversions import Temperature, Cooking


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
            x = Cooking(0, 0)
            x.printConvTable()
        elif menu_choice == '2':
            gallons = int(input('How many gallons to convert to cups? '))
            x = Cooking(gallons, 0)
            x.fromGals()
        elif menu_choice == '3':
            cups = int(input('How many cups to convert to tablespoons? '))
            x = Cooking(0, cups)
            x.fromCups()
        elif menu_choice == 'b':
            mainMenu()
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
            celT = int(input('What degree Celsius? '))
            jeff = Temperature(0, celT)
            jeff.fromCelsius()
        elif menu_choice == '2':
            t = int(input('What degree Fahrenheit? '))

            jeff = Temperature(t, 0)
            jeff.fromFahrenheit()
        elif menu_choice == '3':
            print('Work In Progress bb.')
        elif menu_choice == 'b':
            mainMenu()
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
        print(":stop_sign:\\[q] Exit the program.")

        # Get users choice
        menu_choice = Prompt.ask("Enter your choice", choices=[
                                 '1', '2', '3', 'q', ])

        if menu_choice == '1':
            temperatureMenu()
        elif menu_choice == '2':
            pass
        elif menu_choice == '3':
            cookingMenu()
        elif menu_choice == 'q':
            print('exiting')
            sys.exit()
        else:
            print("You've broken me.")
