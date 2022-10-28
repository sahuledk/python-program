# program to check whether the year is leap year

# Taking the year value
year = int(input("enter the year"))

""" divided by 100 means century years.All the century years are not leap years.
century years divisible by 400 is leap year"""

# checking whether the year is divisible by 4
# if divisible by 4,then checking the probability of being leap year.
if year % 4 == 0:
    if year % 100 and year % 400 == 0:
        # checking whether the number is divisible by both 100 and 400
        # if then it is leap year
        print("it is leap year")
    elif year % 100 == 0 and year % 400 != 0:
        # checking whether the number is divisible by 100 and not by 400
        # then not it is not leap year.
        print("not leap year")
    else:
        # if it is only divided by 4
        # thnn it is not a leap year.
        print("it is a leap year")
else:
    # if not divided by 4 then not leap year.
    print("it's not a leap year")

