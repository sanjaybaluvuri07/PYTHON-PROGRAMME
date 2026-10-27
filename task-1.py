
def validate_password(password):
    errors = []

    # Rule 1: Minimum length
    if len(password) < 8:
        errors.append("Password must contain at least 8 characters.")

    # Rule 2: Character categories
    if not any(c.isupper() for c in password):
        errors.append("Missing an uppercase letter (A-Z).")

    if not any(c.islower() for c in password):
        errors.append("Missing a lowercase letter (a-z).")

    if not any(c.isdigit() for c in password):
        errors.append("Missing a number (0-9).")

    if not any(not c.isalnum() for c in password):
        errors.append("Missing a special character (e.g., @, #, !).")

    # Rule 3: Repetition
    if any(password[i] == password[i + 1]
           for i in range(len(password) - 1)):
        errors.append("Contains consecutive repeated characters.")

    # Rule 4: Prohibited substrings (case-insensitive)
    prohibited = ["password", "admin", "123456"]

    for word in prohibited:
        if word in password.lower():
            errors.append(f"Contains prohibited substring: '{word}'.")

    # Display results
    if errors:
        print(f"\nPassword: {password}")
        print("Status: INVALID")
        for error in errors:
            print("- " + error)
    else:
        print(f"\nPassword: {password}")
        print("Status: VALID")


# Sample password tests
samples = [
    "abc",
    "password123!",
    "Abcdef1!",
    "ABCD123!",
    "Secure@2026",
    "AAbbcc12!"
]

for password in samples:
    validate_password(password)
