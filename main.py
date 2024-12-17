import re

def check_password_strength(password: str) -> str:
    # Initialize score
    score = 0
    
    # Define the minimum length
    min_length = 8

    if len(password) >= min_length:
        score += 1  # Length criterion met


    if re.search(r"[a-z]", password):
        score += 1  # Lowercase letter criterion met


    if re.search(r"[A-Z]", password):
        score += 1  # Uppercase letter criterion met


    if re.search(r"\d", password):
        score += 1  # Digit criterion met


    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1  # Special character criterion met

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    return f"Password score: {score}/5\nPassword strength: {strength}"


password = input("Enter a password: ")
print(check_password_strength(password))
