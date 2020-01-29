print("Using only if sentences, find the highest number no matter which of the three variables has the highest one. To make it simpler, you can assume that the values will always be different to each other.")
print(".............")
print("a=1")
print("b=2")
print("c=3")
print(".............")

a = 1
b = 2
c = 3

if a > b and a > c:
    print("a is the highest number")
elif b > a and b > c:
    print("b is the highest number")
else:
    print("c is the highest number")
