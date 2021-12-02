from rich import table
from rich import inspect
from rich.prompt import Prompt

choice = Prompt.ask("Enter your choice:", choices=['1', '2', '3', '4', '9'])

inspect(table, methods=True)
# help(table)
