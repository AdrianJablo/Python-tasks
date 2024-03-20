from validator_collection import validators

def main():
    address = input("What is your email address? ")
    try:
        ValidEmail = validators.email(address)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()
