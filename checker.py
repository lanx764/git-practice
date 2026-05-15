def check_age(age):
    if not isinstance(age, int):
        print("Please enter a valid number")
    elif age < 0:
        print("Age cannot be negative")
    elif age < 18:
        print("You are a minor")
    elif age >= 18 and age <= 65:
        print("You are an adult")
    elif age > 65:
        print("You are a senior")
    else:
        print("Invalid age")