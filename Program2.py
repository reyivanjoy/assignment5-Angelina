print("Input Three Numbers")
firstNumber = int(input("First Number: "))
secondNumber = int(input("Second Number: "))
thirdNumber = int(input("Third Number: "))
if firstNumber < secondNumber and firstNumber < thirdNumber:
    print(f"{firstNumber} is the lowest number")
else:
    if secondNumber < firstNumber and secondNumber < thirdNumber:
        print(f"{secondNumber} is the lowest number")
    else:
        if thirdNumber < firstNumber and thirdNumber < secondNumber:
            print(f"{thirdNumber} is the lowest number")
        else:
            print("There is no lowest number")
 
