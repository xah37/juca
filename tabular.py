from rich.console import Console
from rich.table import Table
from rich import box


def print_conv_table():
    table = Table(title="Volume Conversion Chart", box=box.HEAVY_EDGE)

    table.add_column("Tsp.", justify="center", style="cyan", no_wrap=True)
    table.add_column("Tbsp.", justify="center",
                     style="bold blue", no_wrap=True)
    table.add_column("Ounces", justify="center", style="bold red",)
    table.add_column("Cups", justify="center",
                     style="bold yellow", no_wrap=True)

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
