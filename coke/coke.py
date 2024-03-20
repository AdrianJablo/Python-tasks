i = 50
while i > 0:
    print(f"Amount Due: {i}")
    inserted = int(input("Insert Coin: "))
    if inserted == 5 or inserted == 10 or inserted == 25:
        change = inserted - i
        i -= inserted
if change == 0 :
    print(f"Change Owed: 0")
else:
    print(f"Change Owed: {change}")
