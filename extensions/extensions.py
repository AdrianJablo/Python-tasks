file = input("Enter file name with extension: ").strip().lower().split(".")[-1]

match file:
    case "gif" | "png" :
        print(f"image/{file}")
    case "txt" :
        print("text/plain")
    case "jpg" | "jpeg" :
        print("image/jpeg")
    case "pdf" | "zip" :
        print(f"application/{file}")
    case _:
       print("application/octet-stream")

