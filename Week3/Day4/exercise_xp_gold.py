# Exercise 1: Upcoming Holiday
import datetime

def upcoming_holiday():
    today = datetime.date.today()
    print(f"Today's date: {today}")
    
    holidays = {
        "New Year's Day": datetime.date(2027, 1, 1),
        "Independence Day": datetime.date(2027, 7, 4),
        "Christmas": datetime.date(2026, 12, 25),
        "Halloween": datetime.date(2026, 10, 31)
    }
    
    future_holidays = {name: d for name, d in holidays.items() if d >= today}
    if not future_holidays:
        print("No upcoming holidays found.")
        return
    
    next_holiday_name = min(future_holidays, key=future_holidays.get)
    next_holiday_date = future_holidays[next_holiday_name]
    days_left = (next_holiday_date - today).days
    
    print(f"The next holiday is {next_holiday_name} in {days_left} days.")

upcoming_holiday()


# Exercise 2: How Old Are You On Jupiter
def calculate_planet_ages(seconds):
    earth_seconds_per_year = 31557600
    earth_years = seconds / earth_seconds_per_year
    
    orbital_periods = {
        "Earth": 1.0,
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132
    }
    
    ages = {}
    for planet, period in orbital_periods.items():
        ages[planet] = round(earth_years / period, 2)
    
    for planet, age in ages.items():
        print(f"{planet}: {age} Earth-years old")

calculate_planet_ages(1000000000)


# Exercise 3: Regular Expression #1
import re

def return_numbers(input_str):
    numbers = "".join(re.findall(r'\d', input_str))
    print(numbers)
    return numbers

return_numbers('k5k3q2g5z6x9bn')


# Exercise 4: Regular Expression #2
import re

def check_name_validity(name):
    pattern = r'^[A-Z][a-z]+ [A-Z][a-z]+$'
    if re.match(pattern, name):
        print(f"'{name}' is a valid name.")
        return True
    else:
        print(f"'{name}' is invalid. Must contain only letters, exactly one space, and each name capitalized.")
        return False

check_name_validity("John Doe")
check_name_validity("john doe")


# Exercise 5: Python Password Generator
import random
import string

def test_password(password):
    if len(password) < 6 or len(password) > 30:
        return False
    has_digit = any(char.isdigit() for char in password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_special = any(char in string.punctuation for char in password)
    return has_digit and has_lower and has_upper and has_special

def generate_password(length):
    digits = string.digits
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    special = string.punctuation
    
    password_chars = [
        random.choice(digits),
        random.choice(lower),
        random.choice(upper),
        random.choice(special)
    ]
    
    all_chars = digits + lower + upper + special
    for _ in range(length - 4):
        password_chars.append(random.choice(all_chars))
        
    random.shuffle(password_chars)
    return "".join(password_chars)

for _ in range(100):
    length = random.randint(6, 30)
    pwd = generate_password(length)
    assert test_password(pwd) == True

def run_password_generator():
    while True:
        try:
            length_input = int(input("Enter password length (between 6 and 30): "))
            if 6 <= length_input <= 30:
                break
            print("Please enter a number between 6 and 30.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    password = generate_password(length_input)
    print(f"Generated Password: {password}")
    print("Reminder: Keep your password in a safe place!")

