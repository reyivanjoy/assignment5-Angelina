print("Input Three Numbers")
a = int(input("First Number: "))
b = int(input("Second Number: "))
c = int(input("Third Number: "))
if a < b and a < c:
    print(f"{a} is the lowest number")
else:
    if b < a and b < c:
        print(f"{b} is the lowest number")
    else:
        if c < a and c < a:
            print(f"{c} is the lowest number")
        else:
            print("There is no lowest number")
 