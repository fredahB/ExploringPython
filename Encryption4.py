import random
while True:
    plainText = input("Please enter your text or 0 to exit: ")
    plainText = plainText.lower()
    if plainText == "0":
        print("Thanks and goodbye!")
        break
    choice = input("Enter e to encrypt or d to decrypt: ")

    output = ""
    dividersList = ["sed", "aaerfcx", "blijare", "iersdf"]
    if choice == "e":
        #encryption code
        for letter in plainText:
            if letter == "a":
                output += random.choice(["txlklkjlu","adljaeriuj", "adkjer","ad4rfrr"])
            elif letter == "b":
                output += random.choice(["dkrs", "dalkje4"])
            elif letter == "c":
                output += random.choice(["foieadce", "adfjrte", "lkdie"])
            elif letter == "d":
                output += random.choice(["kelkjljkr", "dakfljale", "dakje"])
            elif letter == " ":
                output += random.choice(["lkhrdfsgf", "dkljae", "hijrfs"])
            output += random.choice(dividersList)
    elif choice == "d":
        #decryption code
        for divider in dividersList:
            plainText = plainText.replace(divider, " ")
            print(divider, plainText)
        print(plainText)
        wordsList = plainText.split(" ")
        print(wordsList)
        for word in wordsList:
            if word in ["txlklkjlu","adljaeriuj", "adkjer","ad4rfrr"]:
                output = output + "a"
            elif word in ["dkrs", "dalkje4"]:
                output += "b"
            elif word in ["foieadce", "adfjrte", "lkdie"]:
                output += "c"
            elif word in ["kelkjljkr", "dakfljale", "dakje"]:
                output += "d"
            elif word in ["lkhrdfsgf", "dkljae", "hijrfs"]:
                output += " "
    print("Your output is:",output)