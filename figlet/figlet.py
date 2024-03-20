import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    font = choice(figlet.getFonts())
    figlet.setFont(font = font)
elif len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "-font") and sys.argv[2] != "":
        figlet.setFont(font = sys.argv[2])
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

input = input("Input: ")
print(figlet.renderText(input))
