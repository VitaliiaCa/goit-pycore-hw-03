#Task 1
from datetime import datetime
def get_days_from_today(date_str):
    given_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    today = datetime.today().date()
    delta = today - given_date
    return delta.days
def task1():
    result = get_days_from_today('2020-10-09')
    print(result)
task1()


# Task2
import random
def get_numbers_ticket(min_value, max_value, quantity):
    if (
        not isinstance(min_value, int)
        or not isinstance(max_value, int)
        or not isinstance(quantity, int)
        or min_value < 1
        or max_value > 1000
        or min_value >= max_value
        or quantity > (max_value - min_value + 1)
    ):
        return []
    result = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(result)

def task2():
    numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", numbers)


# Task3
import re

def normalize_phone(phone_number: str) -> str:
    phone_number = phone_number.strip()
    if phone_number.startswith('+'):
        cleaned = '+' + re.sub(r'\D', '', phone_number[1:])
    else:
        cleaned = re.sub(r'\D', '', phone_number)

    if cleaned.startswith('+380'):
        return cleaned
    if cleaned.startswith('380'):
        return '+' + cleaned
    if cleaned.startswith('0'):
        return '+38' + cleaned
    return '+38' + cleaned

def task3():
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


  #Task4
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming = []

    for user in users:
        birth_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birth_date.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congrat_date = birthday_this_year
            if congrat_date.weekday() == 5:  # Saturday
                congrat_date += timedelta(days=2)
            elif congrat_date.weekday() == 6:  # Sunday
                congrat_date += timedelta(days=1)

            upcoming.append({
                "name": user["name"],
                "congratulation_date": congrat_date.strftime("%Y.%m.%d")
            })

    return upcoming

def task4():
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Alice Johnson", "birthday": "1995.06.29"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)

def main():
    #task1()
    #task2()
    #task3()
    task4()  

if __name__ == "__main__":
    main()  
 
