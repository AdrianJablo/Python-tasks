from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_birth_date(birth_date)
    except:
        sys.exit("Invalid Date")
    date_bitrh = date(int(year), int(month), int(day))
    today = date.today()
    difrence = today - date_bitrh
    minutes = difrence.days * 24 * 60
    words = p.number_to_words(minutes, andword="")
    print(words.capitalize() + " minutes")

def check_birth_date(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day

if __name__ == "__main__":
    main()
