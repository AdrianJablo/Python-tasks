import random


def main():
    generated = 0
    count_points = 0
    level = get_level()
    while generated != 10:
        generated = int(generated + 1)
        tires = 0
        X = int(generate_integer(level))
        Y = int(generate_integer(level))
        while tires != 3:
            try:
                problem = int(X + Y)
                print(f"{X} + {Y} =",end = " ")
                answer = int(input())

                if answer == problem:
                    count_points = int(count_points + 1)
                    break
                else:
                   print("EEE")
                   tires = int(tires + 1)

                if tires == 3:
                    print(problem)
                    break

            except:
                pass
    print(count_points)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level == 1:
        return random.randint(0,10-1)
    elif level == 2:
        return random.randint(10,100-1)
    elif level == 3:
        return random.randint(100,1000-1)


if __name__ == "__main__":
    main()
