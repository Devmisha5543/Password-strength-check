import re

def check_pas_str(password):
    strength = 0
    message = []

    if len(password) >= 8:
        strength += 1
    else:
        message.append("Password must be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        message.append("Password must contain at least one uppercase letter.")
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        message.append("Password must contain at least one lower case")
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        message.append("Password must contain number")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        message.append("password must contain at least one special character ")
    if strength == 5:
        print("Password is strong")
    elif strength >= 3:
        print("Password moderate")
    else:
        print("Weak password")
    if message:
        print("\nImprovement suggestions:")
        for tip in message:
            print(" -", tip)
    else:
        print("Congratulations 🎉 you've constructed a strong password")

    print(f"\nscore = {strength}/5 ")


print("Password Strength Checker")
while True:
    user_input = input("Enter your password: ")
    if user_input.lower() in ('cancel', 'c', 'exit', 'quit'):
        print("Cancelled.")
        break
    check_pas_str(user_input)
    while True:
        choice = input("\nEnter 1 to retry, 0 to cancel: ").strip()
        if choice == '' or choice == '1':
            break
        if choice == '0':
            print("Cancelled.")
            exit(0)
        print("Please enter '1' to retry or '0' to cancel.")