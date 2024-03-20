import sys
import csv

students = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len (sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"].split(",")
                students.append({"first": name[1].lstrip(),"last": name[0].lstrip(), "house": row["house"]})
    except FileNotFountError:
        sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
    writer.writerow({"first": "first", "last": "last", "house": "house"})
    for student in students:
        writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})
