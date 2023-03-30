monthno = int(input("Enter Month no\n"))
if monthno == 1 or monthno == 3 or monthno == 5 or monthno == 7 or monthno == 8 or monthno == 10 or monthno == 12:
    days = 31,
elif monthno == 4 or monthno == 6 or monthno == 9 or monthno == 11:
    days = 30
elif monthno == 2:
    year = int(input("enter year\n"))
    if year % 400 == 0:
        days = ("Leap Year = 29 days")
    elif year % 4 == 0 and year % 100 != 0:
        days = ("Leap Year = 29 days")
    elif year:
        days = ("not leap year = days 28 ")
else:
    days = "Invalid month no "
print(days)
