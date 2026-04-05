try:
    num1=int(input("Please enter the first number: "))
    num2=int(input("Please enter the second number: "))
    calculation=(num1/num2)
    print(calculation)
except ZeroDivisionError:
    print("Cannot be divisible by 0")
finally:
    print("Calculation done")
     