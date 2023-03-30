# this method 12345676543
# check if a given year is leap year.
year = 2011
if year % 400 == 0:
    print("Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not Leap Year")
