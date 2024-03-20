import sys
import os
import csv
from tabulate import tabulate

dictionary = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len (sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    elif not os.path.exists(sys.argv[1]):
        sys.exit("File does not exist")
    else:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                dictionary.append(row)
print(tabulate(dictionary, "keys", tablefmt="grid"))
