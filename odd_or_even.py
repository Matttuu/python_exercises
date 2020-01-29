print("Make a script that can decide if you entered an odd or even number.")
print("Use the modulus operator %")
print(".............")

value = input("Enter value: ")
y = 2
x = float(value) % y

print(x)

if x == 0:
    print("The number you've entered is an even number")
else:
    print("The number you've entered is an uneven number")
