import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    american_format = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if american_format:
        group = american_format.groups()
        if int(group[1]) > 12 or int(group[5]) > 12:
            raise ValueError
        first = convert_format(group[1],group[2],group[3])
        second = convert_format(group[5],group[6],group[7])
        return first + " to
        " + second
    else:
        raise ValueError

def convert_format(houre,minute,time):
    if time == "PM":
        if int(houre) == 12:
            new_houre = 12
        else:
            new_houre = int(houre) + 12
    else:
        if int(houre) == 12:
            new_houre = 0
        else:
            new_houre = int(houre)
    if minute == None:
        new_minute = ":00"
        new_time = f"{new_houre:02}" + new_minute
    else:
        new_time = f"{new_houre:02}" + ":" + minute
    return new_time


if __name__ == "__main__":
    main()
