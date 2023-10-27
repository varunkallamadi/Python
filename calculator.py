def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if x == 0 or y == 0:
        print("You Can't Divide")
    else:
       return x/y

print("select operation: ")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")


choice = input("enter choice(1/2/3/4):")
n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))


if choice == "1":
    print(n1, "+", n2, "=", add(n1, n2))
elif choice == "2":
    print(n1, "-", n2, "=", substract(n1, n2))
elif choice == "3":
    print(n1, "*", n2, "=", multiply(n1, n2))
elif choice == "4":
    print(n1, "/", n2, "=", divide(n1, n2))
else:
    print("invalid")
