import re


def evaluate_password(candidate):
    strength = 0
    messages = []

    if len(candidate) >= 8:
        strength += 1
    else:
        messages.append("Password must be at least 8 characters long.")

    if re.search(r'[A-Z]', candidate):
        strength += 1
    else:
        messages.append("Password must contain at least one uppercase letter.")
    if re.search(r'[a-z]', candidate):
        strength += 1
    else:
        messages.append("Password must contain at least one lowercase letter.")
    if re.search(r'[0-9]', candidate):
        strength += 1
    else:
        messages.append("Password must contain at least one number.")
    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', candidate):
        strength += 1
    else:
        messages.append("Password must contain at least one special character.")

    if strength == 5:
        verdict = "Strong"
    elif strength >= 3:
        verdict = "Moderate"
    else:
        verdict = "Weak"

    return strength, verdict, messages


def check_pas_str(candidate):
    strength, verdict, messages = evaluate_password(candidate)

    print(f"\nPassword status: {verdict}")

    if messages:
        print("Improvement suggestions:")
        for tip in messages:
            print(" -", tip)
    else:
        print("Congratulations 🎉 you've constructed a strong password")

    print(f"Score = {strength}/5")
    return strength, verdict, messages


def run_interface():
    print("=== Password Strength Checker ===")
    print("Type 'help' to view password rules or 'quit' to exit.")

    while True:
        user_input = input("\nEnter your password (or command): ").strip()
        command = user_input.lower()

        if command in ('cancel', 'c', 'exit', 'quit'):
            print("Cancelled.")
            break
        if command in ("help", "h"):
            print("\nPassword rules:")
            print(" 1. At least 8 characters")
            print(" 2. At least one uppercase letter")
            print(" 3. At least one lowercase letter")
            print(" 4. At least one number")
            print(" 5. At least one special character")
            continue
        if not user_input:
            print("Please enter a password or a command.")
            continue

        check_pas_str(user_input)


if __name__ == "__main__":
    run_interface()
