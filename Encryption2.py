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
                output += "txlku"
            elif letter == "b":
                output += "dkers"
            elif letter == "c":
                output += "foie3"
            elif letter == "d":
                output += "msker"
            elif letter == " ":
                output += "lkhrf"
    elif choice == "d":
        #decryption code
        #plainText[0:5]
        #plainText[5:10]
        #plainText[10:15]
        currentIndex = 0
        while currentIndex < len(plainText):
            word = plainText[currentIndex:currentIndex+5]
            print(currentIndex, word)
            currentIndex += 5

            if word == "txlku":
                output = output + "a"
            elif word == "dkers":
                output += "b"
            elif word == "foie3":
                output += "c"
            elif word == "msker":
                output += "d"
            elif word == "lkhrf":
                output += " "
    print("Your output is:",output)