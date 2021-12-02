from rich.console import Console
from rich.table import Table
from rich import box


# ADD SOME MORE COOKING MATH
# MAYBE USE THE FUNC FOR C TO F OR F TO C


def gal_to_cups(n):
    return f"{16/n} cups"


def cups_to_tbsp(n):
    return f"{16*n} tbsp"


def print_conv_table():
    table = Table(title="Volume Conversion Chart")

    table.add_column("Tsp.", justify="right", style="cyan", no_wrap=True)
    table.add_column("Tbsp.", justify="right", style="cyan", no_wrap=True)
    table.add_column("Ounces", justify="center", style="red",)
    table.add_column("Cups", justify="center", style="red", no_wrap=True)

    table.add_row(
        '3',
        '1',
        '1/2',
        '1/16'
    )
    table.add_row(
        '12',
        '4',
        '2',
        '1/4'
    )
    table.add_row(
        '24',
        "8",
        "4",
        "1/2",
    )
    table.add_row(
        '48',
        '16',
        '8',
        '1',
    )

    console = Console()
    console.print(table)


print_conv_table()
