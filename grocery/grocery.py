d = {}
while True:
    try:
        item = input().upper()
        if item not in d:
            d[item] = 0
        d[item] += 1
    except EOFError:
        break
    except KeyError:
        pass
for key,value in sorted(d.items()):
    print(f"{value} {key}")
