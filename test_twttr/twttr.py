def main():
    word = input("Input: ").lower()
    print(f"Output: {shorten(word)}")


def shorten(word):
    vowels_omitted = ['a','e','i','o','u']
    omitted_word = ""
    for t in word:
        for v in vowels_omitted:
            if t.lower() == v:
                t = ""
                break
        omitted_word = omitted_word + t

    return omitted_word

if __name__ == "__main__":
    main()

