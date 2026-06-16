import re


def evaluate_strength(candidate):
    strength = 0
    messages = []

    if len(candidate) >= 8:
        strength += 1
    else:
        messages.append("Must be at least 8 characters long.")

    if re.search(r'[A-Z]', candidate):
        strength += 1
    else:
        messages.append("Must contain at least one uppercase letter.")
    if re.search(r'[a-z]', candidate):
        strength += 1
    else:
        messages.append("Must contain at least one lowercase letter.")
    if re.search(r'[0-9]', candidate):
        strength += 1
    else:
        messages.append("Must contain at least one number.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', candidate):
        strength += 1
    else:
        messages.append("Must contain at least one special character.")

    if strength == 5:
        verdict = "Strong"
    elif strength >= 3:
        verdict = "Moderate"
    else:
        verdict = "Weak"

    return strength, verdict, messages


def show_feedback(strength, verdict, messages):
    print(f"\nStrength status: {verdict}")

    if messages:
        print("Improvement suggestions:")
        for tip in messages:
            print(" -", tip)
    else:
        print("Congratulations 🎉 you've constructed a strong password.")

    print(f"Score = {strength}/5")


def run_interface():
    print("=== Password Strength Checker ===")
    print("Type 'help' to view strength rules or 'quit' to exit.")

    while True:
        user_input = input("\nEnter text (or command): ").strip()

        if user_input.lower() in ('cancel', 'c', 'exit', 'quit'):
            print("Cancelled.")
            break
        if user_input.lower() in ("help", "h"):
            print("\nStrength rules:")
            print(" 1. At least 8 characters")
            print(" 2. At least one uppercase letter")
            print(" 3. At least one lowercase letter")
            print(" 4. At least one number")
            print(" 5. At least one special character")
            continue
        if not user_input:
            print("Please enter text or a command.")
            continue

        strength, verdict, messages = evaluate_strength(user_input)
        show_feedback(strength, verdict, messages)


if __name__ == "__main__":
    run_interface()
