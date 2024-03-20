import sys
from os.path import splitext
from PIL import Image, ImageOps

def check_file(f):
    if f in [".jpg", ".jepg", ".png"]:
        return True
    return False

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    file_one = splitext(sys.argv[1])
    file_two = splitext(sys.argv[2])
    if check_file(file_one[1]) == False:
        sys.exit("Invalid input")
    elif check_file(file_two[1]) == False:
        sys.exit("Invalid input")
    elif file_one[1].lower() != file_two[1].lower():
        sys.exit("Input and output have different extensions")
    else:
        try:
            imagefile = Image.open(sys.argv[1])
        except:
            sys.exit("Input does not exist")

        shirtfile = Image.open("shirt.png")
        size = shirtfile.size
        muppet = ImageOps.fit(imagefile,size)
        muppet.paste(shirtfile,shirtfile)
        muppet.save(sys.argv[2])
