#exercise happy birthday

user_date = (input("enter you birhtdate in this specify format: DD/MM/YY: "))

birth_year = int(user_date[-4:])

current_year = 2026
age = current_year - birth_year

candles_count = age % 10

candles_line = "i" * candles_count
center_candles = candles_line.center(14, "_")

cake =       f""" 
          ___{center_candles}___
              |:H:a:p:p:y:|
            __|___________|__
           |^^^^^^^^^^^^^^^^^|
           |:B:i:r:t:h:d:a:y:|
           |                 |
           ~~~~~~~~~~~~~~~~~~~"""

print(f"you birthday is: {user_date} and\n {cake}")