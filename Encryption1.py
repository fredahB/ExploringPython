while True:
    plainText = input("Please enter your text or 0 to exit: ")
    plainText = plainText.lower()
    if plainText == "0":
        print("Thanks and goodbye!")
        break
    choice = input("Enter e to encrypt or d to decrypt: ")

    output = ""
    if choice == "e":
        #encryption code
        for letter in plainText:
            if letter == "a":
                output = output + "t"
            elif letter == "b":
                output += "d"
            elif letter == "c":
                output += "x"
            elif letter == "d":
                output += "k"
            elif letter == " ":
                output += "*"
    elif choice == "d":
        #decryption code
        for letter in plainText:
            if letter == "t":
                output = output + "a"
            elif letter == "d":
                output += "b"
            elif letter == "x":
                output += "c"
            elif letter == "k":
                output += "d"
            elif letter == "*":
                output += " "
    print("Your output is:",output)