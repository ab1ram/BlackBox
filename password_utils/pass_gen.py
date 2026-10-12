import string
import secrets


def generate_pwd(
        length,
        uppercase_count=0,
        lowercase_count=0,
        digits_count=0,
        symbols_count=0
        ):
    # Validate password length
    if not isinstance(length, int) or isinstance(length, bool):
        raise TypeError("Password length must be an integer")

    if not 4 <= length <= 64:
        raise ValueError("Password length must be between 4 and 64")
    
    # Validate minimum character counts
    counts = [
        uppercase_count,
        lowercase_count,
        digits_count,
        symbols_count
    ]

    if any(not isinstance(count, int) or isinstance(count, bool)
        for count in counts):
        raise TypeError("Character counts must be integers")
            
    if any(count < 0 for count in counts):
        raise ValueError("Character counts cannot be negative")

    if sum(counts) > length:
        raise ValueError("Minimum character counts exceed password length")

    # Define character categories
    categories = [
        (string.ascii_uppercase, uppercase_count),
        (string.ascii_lowercase, lowercase_count),
        (string.digits, digits_count),
        (string.punctuation, symbols_count)
    ]
    
    # Include only categories with a minimum above zero
    selected_categories = []
        
    for characters, count in categories:
        if count > 0:
            selected_categories.append(characters)

    if not selected_categories:
        raise ValueError("Select at least one character category")

    # Generate the minimum required characters
    password = []

    for characters, count in categories:
        for _ in range(count):
            password.append(secrets.choice(characters))

    # Fill the remaining password length
    while len(password) < length:
        characters = secrets.choice(selected_categories)
        password.append(secrets.choice(characters))

    # Shuffle and return
    secrets.SystemRandom().shuffle(password)
    return "".join(password)

