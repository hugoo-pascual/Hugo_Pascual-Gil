'''import datetime

a = datetime.date(2020, 8, 31)
print(a)
print(type(a))

b= datetime.date.today()
print(b)

print(a.year)
print(a.month)
print(a.day)

c = datetime.time(12, 18, 35, 5867)
print(c)
print(type(c))

d = datetime.time(23, 15, 30)
e = datetime.time(15, 20, 00)
f = datetime.time(22, 00, 00)

print(d)
print(e)
print(f)'''


#Exercise 1
'''import datetime

date = input()
months = ["January", "February", "March", "April", "May",
          "June", "July", "August", "September", "October",
          "November", "December"]

month = date[:2]
months = months[int(month) - 1]
print(months)

day = date[3:5]

year = date[6:11]

time = date[11:17]

time_day = date[17:]


date = datetime.datetime(month, day, year, time, time_day)
print(date)'''



#Exercise 2

'''import datetime

import datetime

#Name the variables

time = datetime.datetime.today()

total = 0

year = int(input("Enter year of birth: "))

if year > time.year:
    year = int(input("Enter a year of birth: "))

month = int(input("Enter month of birth: "))

if month > 12:
    month = int(input("Enter month of birth: "))

day = int(input("Enter day of birth: "))

if month == 4 or month == 6 or month == 8 or month == 10 or month == 12:
    if day > 30:
        day = int(input("Enter day of birth: "))
elif month == 2:
    if day >= 29:
        day = int(input("Enter day of birth: "))
else:
    if day > 31:
        day = int(input("Enter day of birth: "))



#Years to days

year =  (time.year - year) * 365

#Month to days

month = (12 - month) * 30.5

#Final result
total = day + year + int(month)
print(total)'''

#Exercise 3

import datetime


'''day = ['monday', 'tuesday', 'wednesday',
       'thursday', 'friday', 'saturday', 'sunday']'''

def count_friday_13(year):
    friday_13_counter = 0

    for month in range(1, 13):
        if datetime.date(year, month, 13).weekday() == 4:
            print(f"Friday th 13th is {year}-{month}-13")
            friday_13_counter += 1
            
    return friday_13_counter


while True:
    try:
        year = int(input("Enter a year: "))
        if year > 2025:
            year = int(input("Enter a valid integer for the year: "))
                       
        count = count_friday_13(year)
        print(f"In {year} there where {count} Fridays the 13th")
        break

    except ValueError:
        print(f"Enter a valid integer for the year")







