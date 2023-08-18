l1 = ["hello", "there", 57, "23", 3,7,3,5]
print(l1[1])
print(l1)
print(l1[:])
print(l1[2:6])
print(l1[:6])
print(l1[6:])
print(l1[-5:-1])

l1[4] = "new item"
print(l1)
l2 = [0,1,2,3,4,5,6,7,8,9,10]
print([1,2] in l2)
print(len(l2))
print(max(l2))
print(min(l2))
print(sum(l2))

l1.append("python")
print(l1)
l1.append([1,2,3])
print(l1)
l1.extend([1,2,3])
print(l1)
l1.clear()
print(l1)
l1 = [2,3,1,4,3,2,3,4,5,6,3,7]
print(l1.count(3))

nts = 4
if nts in l1:
    print(l1.index(nts))
else:
    print(-1)
x = l1.pop()
print(x, l1)
x = l1.pop()
print(x, l1)
x = l1.pop()
print(x, l1)
l1.remove(3)
print(l1)

ntr = 2
while ntr in l1:
    l1.remove(ntr)
print(l1)
l1.reverse()
print(l1)
l1.sort()
print(l1)
l1.sort(reverse=True)
l1.sort()
l1.reverse()
print(l1)

l3 = [1,2,3,4]
l4 = l3[:]
print(l3,l4)
l3.append("New Item")
print(l3,l4)
l3.append(77)
print(l3,l4)
l4.extend([5,6,7])
print(l3,l4)

s = "This is a string"
l1 = list(s)
print(l1)
l2 = s.split()
print(l2)
l3 = s.split("s")
print(l3)

s1 = "".join(l1)
print(s1)
s2 = " ".join(l2)
print(s2)
s3 = "s".join(l3)
print(s3)

