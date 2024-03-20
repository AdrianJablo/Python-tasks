def main():
    mass = int(input("m: "))
    print(f"E: {energy(mass)}")

def energy(m):
    return m*pow(300000000,2)

main()
