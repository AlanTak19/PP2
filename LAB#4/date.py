from datetime import timedelta, datetime
import time

#Write a Python program to subtract five days from current date.
today = datetime.now()
print(today - timedelta(days = 5))

#Write a Python program to print yesterday, today, tomorrow.
yesterday = (today - timedelta(days = 1))
tomorrow = (today + timedelta(days = 1))
print(f"Yesterday: {yesterday}, Today: {today}, Tomorrow: {tomorrow}")

#Write a Python program to drop microseconds from datetime.
date = today.replace(microsecond=0)
print(date)

#Write a Python program to calculate two date difference in seconds.
n = int(input())
date1 = today
date2 = today + timedelta(days = n)
print(f"Difference between {n} days:", (date2-date1).total_seconds())
