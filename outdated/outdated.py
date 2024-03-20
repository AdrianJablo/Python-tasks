months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")

        if "/" in date:
            month_number,day,year = map(int,date.split("/"))
            if not 1 <= month_number <= 12:
                continue
            elif not 1 <= day <= 31:
                continue

        elif "," in date:
            month_day, year = date.split(", ")
            mon, day = month_day.split(" ")
            day = int(day)

            if not 1 <= day <= 31:
                continue

            for month in months:
                if mon.lower() == month.lower():
                    month_number = months.index(month) + 1
        else:
            continue

        day = int(day)
        year = int(year)

        print(f"{year}-{month_number:02}-{day:02}")
        break

    except ValueError:
        pass

