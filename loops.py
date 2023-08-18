x = 2
#print(x)
x = x + 2
#print(x)
x += 2
#print(x)

n = 5
while n > 0:
    print(n)
    n -= 1
print("Blastoff!")

x = 10
while x < 1000:
    if x%7 == 0:
        print(x)
    x += 1
print("All Done!")

x = 0
total = 0
while x <= 100:
    total += x
    x += 1
print("Your total sum is:", total)

name = "Fredah"
for letter in name:
    print(letter)

l1 = [1,2,3,4,5,6,7,8,9,10]
for num in l1:
    print(num)

for i in range(5,0,-1):
    print(i)
print("Blastoff!")

for i in range(1000):
    if i%8 == 0:
        print(i)
print("All Done!")

total = 0
for num in range(101):
    total += num #total = total + num
print("Your total sum is:", total)

print(list(range(101)))

l1 = [2,4,3,5,4,3,4,3]
for num in l1:
    print(num)
    if num != 3:
        print("Not the one")
        continue
    print("found it!")
    break

