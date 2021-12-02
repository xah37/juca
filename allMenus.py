import sys
from rich import print

# Cute things?
OFFSET_CHAR = '\u2582'
PROMPT_ICON = '\u21E5 '


# TO DO
# REDO PROMP WITH RICH
# Finish menu options

def temp_menu():
    """Temperature conversion menu"""
    header = "Temperature Conversions Menu"
    print(header.center(50, OFFSET_CHAR))


def currency_menu():
    header = "Currency Conversion Menu"
    print(header.center(50, OFFSET_CHAR))


def cooking_menu():
    header = "Cooking Conversion Menu"
    print(header.center(50, OFFSET_CHAR))


def print_main_menu():
    """Emulate a 'main' menu"""
    header = "Main Menu"
    print(header.center(50, OFFSET_CHAR))
    print("""
    1. TEMPERATURE / WEATHER
    2. CURRENCY
    3. COOKING
    4. PLACEHOLDER

    9. EXIT PROGRAM
    """)


def menu():
    print_main_menu()
    menu_choice = 0

    while menu_choice != 9:
        menu_choice = int(input(PROMPT_ICON))

        if menu_choice == 1:
            temp_menu()
            break
        elif menu_choice == 2:
            currency_menu()
            break
        elif menu_choice == 3:
            cooking_menu()
            break
        elif menu_choice == 4:
            pass
        elif menu_choice == 9:
            print('Exiting')
            sys.exit()
