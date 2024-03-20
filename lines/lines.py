import sys
import os

count = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len (sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
    elif not os.path.exists(sys.argv[1]):
        sys.exit("File does not exist")
    else:
       with open(sys.argv[1],"r") as file:
           for line in file:
               line = line.lstrip()
               if line.startswith("#"):
                   continue
               elif line == "":
                   continue
               else:
                   count = count + 1
print(count)
