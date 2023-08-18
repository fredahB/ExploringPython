while True:
    plainText = input("Please enter your text or 0 to exit: ")
    plainText = plainText.lower()
    if plainText == "0":
        print("Thanks and goodbye!")
        break
    choice = input("Enter e to encrypt or d to decrypt: ")

    output = ""
    divider = "sed"
    if choice == "e":
        #encryption code
        for letter in plainText:
            if letter == "a":
                output += "txlklkjlu"
            elif letter == "b":
                output += "dkrs"
            elif letter == "c":
                output += "foieadcefasdf3"
            elif letter == "d":
                output += "kelkjljkr"
            elif letter == " ":
                output += "lkhrdfsgf"
            output += divider
    elif choice == "d":
        #decryption code
        wordsList = plainText.split(divider)
        print(wordsList)
        for word in wordsList:
            if word == "txlklkjlu":
                output = output + "a"
            elif word == "dkrs":
                output += "b"
            elif word == "foieadcefasdf3":
                output += "c"
            elif word == "kelkjljkr":
                output += "d"
            elif word == "lkhrdfsgf":
                output += " "
    print("Your output is:",output)