# TO DO

# WRITE A BANNER PICKER USING RANDOM

from rich import print

import random as r

banner1 = """
[bold red]
     _ _   _  ___   _
  _ | | | | |/ __| /_\\
 | || | |_| | (__ / _ \\
  \__/ \___/ \___/_/ \_\\

[/]
"""
banner2 = """

[bold magneta]
 _______ _______ _______ _______
|\     /|\     /|\     /|\     /|
| +---+ | +---+ | +---+ | +---+ |
| |   | | |   | | |   | | |   | |
| |J  | | |U  | | |C  | | |A  | |
| +---+ | +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|/_____\|
[/]
"""

banner3 = """
[cyan]
    _____  __    __   ______    ______
   |     \|  \  |  \ /      \  /      \\
    \$$$$$| $$  | $$|  $$$$$$\|  $$$$$$\\
      | $$| $$  | $$| $$   \$$| $$__| $$
 __   | $$| $$  | $$| $$      | $$    $$
|  \  | $$| $$  | $$| $$   __ | $$$$$$$$
| $$__| $$| $$__/ $$| $$__/  \| $$  | $$
 \$$    $$ \$$    $$ \$$    $$| $$  | $$
  \$$$$$$   \$$$$$$   \$$$$$$  \$$   \$$


[/]
"""

banner4 = """
[purple]
     ██╗██╗   ██╗ ██████╗ █████╗
     ██║██║   ██║██╔════╝██╔══██╗
     ██║██║   ██║██║     ███████║
██   ██║██║   ██║██║     ██╔══██║
╚█████╔╝╚██████╔╝╚██████╗██║  ██║
 ╚════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝
[/]
"""

banner5 = """

========================================
=====    ==  ====  ====     ======  ====
======  ===  ====  ===  ===  ====    ===
======  ===  ====  ==  =========  ==  ==
======  ===  ====  ==  ========  ====  =
======  ===  ====  ==  ========  ====  =
======  ===  ====  ==  ========        =
=  ===  ===  ====  ==  ========  ====  =
=  ===  ===   ==   ===  ===  ==  ====  =
==     =====      =====     ===  ====  =
========================================
"""

x = [banner2, banner1, banner3, banner4, banner5, ]

print(r.choice(x))