def main():
    greeting = input("Greeting: ").lower().strip()
    print(f"${value(greeting)}")


def value(greeting):
    if 'hello' in greeting.lower():
        return int(0)
    elif greeting.lower().find('h') == 0:
        return int(20)
    else:
        return int(100)

if __name__ == "__main__":
    main()
