#sequential steps
x = 2
print(x)
x = x + 2
print(x)

#conditional steps
x = 15
if x < 10:
    print("Smaller")
if x > 20:
    print("Bigger")
print("Finish!")

#repeated steps
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")

#operators
x = 10
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)
print(y)
print(y**2)

#type conversions
name = "Fredah"
surname = "Banda"
print("hello", name, surname, 11)

print("hello" + str(3))
print(501.7 + int("124"))
print(10 + float("2.5"))

age = "17.5"
print("At your next birthday you will turn: " + str(int(float(age)) + 1))

print(int(float("12.99")))

ntc = 12.3
wholeNumber = int(ntc)
if ntc%wholeNumber >= 0.5:
    newAge = wholeNumber + 1
else:
    newAge = wholeNumber
print(ntc, wholeNumber, newAge)

