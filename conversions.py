from rich import print
from rich.console import Console
from rich.table import Table
from rich import box


class Temperature():

    def __init__(self, t, cels):
        self.t = t
        self.cels = cels

    def fromCelsius(self):
        print(f"{self.cels}\u00b0 celsius is {(self.cels * 9/5)+32}\u00b0 fahrenheit.")
        # print((self.cels * 9/5)+32)

    def fromFahrenheit(self):
        print(f"{self.t}\u00b0 fahrenheit is {(self.t - 32) * 5/9}\u00b0 celsius.")
        # print((self.t - 32) * 5/9)


class Cooking():

    def __init__(self, gals, cups):
        self.gals = gals
        self.cups = cups

    def fromGals(self):
        print(f'{self.gals} gallons is {self.gals*16} cups.')

    def fromCups(self):
        print(f"{self.cups} cups is {self.cups*16} tablespoons.")

    def printConvTable(self):
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
