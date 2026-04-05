
try:
    age = int(input("What is your age: "))
    if 0 < age <= 120:
        print("This is a valid age.")
    else:
        raise ValueError("Age must be between 1 and 120.")
except ValueError as e:  
    print("Invalid input: ",e,"Please try again.")

finally:
    if age%2==0:
        print("This is an even age.")
    else:
        print("This is an odd age.")
