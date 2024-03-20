def main():
    time = input("What time is it? ")
    convertime = convert(time)
    if 7.0 <= convertime <= 8.0:
        print("breakfast time")
    elif 12.0 <= convertime <= 13.0:
        print("lunch time")
    elif 18.0 <= convertime <= 19.0:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    convertTofloat = float((int(hours) * 60 + int(minutes))/60)
    return convertTofloat

if __name__ == "__main__":
    main()
