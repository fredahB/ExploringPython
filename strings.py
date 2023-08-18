s = "Thisisastring"
print(len(s))
for i in range(len(s)):
    print(s[i])

for letter in s:
    print(letter)

print(s[0])
print(s[0:5])
print(s[:7])
print(s[6:])
print(s[-4:])
print(s[10])
print(s[:])
#s[2] = "o" - won't work, no item assignment for strings
print(s.count("is"))
print(s.count("is",5))
print(s.count("is",6,8))
print(s.lower())
print(s.upper())
print(s)
s = s.upper()
print(s)
print(s.islower())
print(s.isupper())

print(s)
print(s.find("IS"))
print(s.find("IS",4))
print(s.find("IS",6,8))

print(s.index("IS"))
#print(s.index("IS",5))
#print(s.index("IS",6,8))

if "TOOLS" in s:
    print(s.index("TOOLS"))
else:
    print(-1)

print(s.replace("IS", "OOOOO"))
print(s)
print(s.startswith("THI"))
print(s.endswith("RING"))
name = "         Fredah          Banda         "
#name = input("Please enter name: ")
print("Orginal: Hello", name, "how are you?")
print("lstrip(): Hello", name.lstrip(), "how are you?")
print("rstrip(): Hello", name.rstrip(), "how are you?")
print("strip(): Hello", name.strip(), "how are you?")
print(s.isdigit())
print(s.isalpha())
print(s.isalnum())

#a-x,b-c,c-w
pt = "abc"
et = pt.replace("a","#").replace("b","(").replace("c", "2")
print(et)


