# Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        curr_name = self.currency if self.currency.endswith('s') else self.currency + 's'
        return f"{self.amount} {curr_name}"

    def __repr__(self):
        curr_name = self.currency if self.currency.endswith('s') else self.currency + 's'
        return f"{self.amount} {curr_name}"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        raise TypeError("Unsupported type for addition")

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        else:
            raise TypeError("Unsupported type for in-place addition")
        return self

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
# print(c1 + c3)


# Exercise 2: Import
def sum_two_numbers(num1, num2):
    result = num1 + num2
    print(result)
    return result

sum_two_numbers(5, 10)


# Exercise 3: String module
import string
import random

letters = string.ascii_letters
random_string = "".join(random.choice(letters) for _ in range(5))
print(random_string)


# Exercise 4: Current Date
import datetime

def display_current_date():
    current_date = datetime.date.today()
    print(current_date)

display_current_date()


# Exercise 5: Amount of time left until January 1st
def time_until_new_year():
    now = datetime.datetime.now()
    next_year = now.year + 1
    new_year = datetime.datetime(next_year, 1, 1)
    time_left = new_year - now
    print(time_left)

time_until_new_year()


# Exercise 6: Birthday and minutes
def minutes_lived(birthdate_str):
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")
    now = datetime.datetime.now()
    difference = now - birthdate
    minutes = difference.total_seconds() / 60
    print(f"You have lived for approximately {int(minutes):,} minutes.")

minutes_lived("1995-05-15")


# Exercise 7: Faker Module
from faker import Faker

fake = Faker()

def generate_users(num_users):
    users_list = []
    for _ in range(num_users):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users_list.append(user)
    return users_list

users = generate_users(3)
print(users)