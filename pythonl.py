year =input("enter the year:")
if (year % 400 == 0) and (year % 100 == 0):
    print("%d is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print( "%dis a leap year".format(year))
else:
    print("%d is not a leap year".format(year))