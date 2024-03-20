camelCase = input("camelCase: ")
print("snake_case: ",end="")
for i in camelCase:
    if i.isupper():
        print(f"_{i.lower()}",end="")
    else:
        print(i.lower(),end="")
print()
