while True:
    try:
        fraction = input("Fraction: ")
        x,y = fraction.split("/")
        output = float((int(x)/int(y))*100)
        if int(x) <= int(y):
            if output <= 1.0:
               print("E")
               break
            elif output >= 99.0:
                print("F")
                break
            else:
                print(f"{round(output)}%")
                break
        else:
            pass

    except (ValueError,ZeroDivisionError):
        pass

