import random
while True:
    plaintext = input("please enter your text or 0 to exit:")
    plaintext = plaintext.lower()
    if plaintext == "0":
        print("Thanks and goodbye")
        break
    choice = input("Enter e to encrypt or d to decrypt:")

    output = ""
    dividers = ["sed","kiop","rfgvl"]
    if choice == "e":
       # encryption code
        for letter in plaintext:
            if letter == "a":
                output += random.choice(["ztlui","rghtysf","thbncmxd","jklhg"])
            elif letter == "b":
                output += random.choice(["youit","ikjuhy"])
            elif letter == "c":
                output += random.choice(["xtrye","opkli"])
            elif letter == "d":
                output += random.choice(["wiiun","ortgh","hjkbvg"])
            elif letter == "e":
                output += "vince"
            elif letter == "f":
                output += "utrga"
            elif letter == "g":
                output += "teryu"
            elif letter == "h":
                output += "sihkc"
            elif letter == "i":
                output += "races"
            elif letter == "j":
                output += "quiop"
            elif letter == "k":
                output += "pertw"
            elif letter == "l":
                output += "oijkn"
            elif letter == "m":
                output += "nhlnb"
            elif letter == "n":
                output += "modfv"
            elif letter == "o":
                output += "lolop"
            elif letter == "p":
                output += "kjhvr"
            elif letter == "q":
                output += "jagaf"
            elif letter == "r":
                output += "icere"
            elif letter == "s":
                output += "horse"
            elif letter == "t":
                output += "grvhg"
            elif letter == "u":
                output += "fartg"
            elif letter == "v":
                output += "ereli"
            elif letter == "w":
                output += "drtrg"
            elif letter == "x":
                output += "catde"
            elif letter == "y":
                output += "bxzas"
            elif letter == "z":
                output += "amnhj"
            output += random.choice(dividers)

    elif choice == "d":
        # decryption code
        for divider in dividers:
            plaintext = plaintext.replace(divider," ")
            print(divider, plaintext)
        print(plaintext)
        wordsList = plaintext.split(" ")
        print(wordsList)
        for word in wordsList:
         if word == "ztlui":
            output = output + "a"
         elif word == "youit":
            output += "b"
         elif word == "xtrye":
            output += "c"
         elif word == "wiiun":
            output += "d"
         elif word == "vince":
            output += "e"
         elif word == "utrga":
            output += "f"
         elif word == "teryu":
            output += "g"
         elif word == "sihkc":
            output += "h"
         elif word == "races":
            output += "i"
         elif word == "quiop":
            output += "j"
         elif word == "pertw":
            output += "k"
         elif word == "oijkn":
            output += "l"
         elif word == "nhlnb":
            output += "m"
         elif word == "modfv":
            output += "n"
         elif word == "lolop":
            output += "o"
         elif word == "kjhvr":
            output += "p"
         elif word == "jagaf":
            output += "q"
         elif word == "icere":
            output += "r"
         elif word == "horse":
            output += "s"
         elif word == "grvhg":
            output += "t"
         elif word == "fartg":
            output += "u"
         elif word == "ereli":
            output += "v"
         elif word == "drtrg":
            output += "w"
         elif word == "catde":
            output += "x"
         elif word == "bxzas":
            output += "y"
         elif word == "amnhj":
            output += "z"
    print("your output is:", output)