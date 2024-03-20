def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def start_with(s):
    if s[0:2].isalpha():
        return True
    else:
        return False

def has_len_characters(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def center_not_number_in_end(s):
    center_index = int(len(s)/2)-1
    center_char = s[center_index]
    if (center_char.isalpha()) and (s[center_index:len(s)-1].isalnum()) and (s[center_index+1] != '0'):
        return True
    else:
        return False

def has_no_marks(s):
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~"
    if any(char in punctuation for char in s):
        return False
    else:
        return True

def is_valid(s):
    if start_with(s) and has_len_characters(s) and center_not_number_in_end(s) and has_no_marks(s):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
