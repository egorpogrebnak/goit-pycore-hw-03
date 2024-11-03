from datetime import datetime
from datetime import timedelta
import random
import re

#Завдання 1

def get_days_from_today(date):
    try:
        today_date = datetime.today()
        given_date = datetime.strptime(date, '%Y-%m-%d')
        
        given_date = given_date.toordinal()
        today_date = today_date.toordinal()

        diff = given_date - today_date
        return diff
    except ValueError:
        print(f"{date} має хибний формат")
        return None

#Тепер завдання 2
def get_numbers_ticket(min, max, quantity):
    numbers_set = set()
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)

        if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
            print("Хибні вхідні дані. Спробуйте знову: min - не менше 1, max - не більше 1000, quantity - між min та max")
            return numbers_set
        
        while len(numbers_set) < quantity:
            numbers_set.add(random.randint(min, max))
        
        return sorted(numbers_set)
    
    except ValueError:
        print("Вхідні дані мають хибний формат")
        return numbers_set

#Тепер завдання 3
def normalize_phone(phone_number):
    phone_number = re.sub(r"[^\d+]","",phone_number.strip())
    if not phone_number.startswith('+'):
        if phone_number.startswith('380'):
            phone_number = '+' + phone_number
        else:
            phone_number = '+38' + phone_number

    return phone_number



#Тепер завдання 4
def get_upcoming_birthdays(users):
    date_today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:

        birthday_day = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        upcoming_birth = datetime(date_today.year, birthday_day.month, birthday_day.day).date()
        
        if upcoming_birth < date_today:
            upcoming_birth = datetime((date_today.year+1), birthday_day.month, birthday_day.day).date()
        
        days_left = (upcoming_birth - date_today).days

        if 0 <= days_left <= 7:
            if upcoming_birth.weekday() > 4:
                congratulation_date = upcoming_birth + timedelta(days=(7-upcoming_birth.weekday))
            else: 
                congratulation_date = upcoming_birth
        
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays
