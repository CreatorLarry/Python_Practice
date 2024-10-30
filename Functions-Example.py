# Number of days per month. First value placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31 , 30, 31, 30, 31] # Days of the months through the year
# Note that the zero is there since positions start from 0 hence prevents an error when month position is entered
# First Function
def is_leap(year):  # Function determines if a year is a leap year and takes one argument which is to be determined
    # Return True for Leap years, false for non-leap years

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) #calculation of a leap year

# Second Function
def days_in_month(year, month):
    # Return number of days in that month in that year
    # 2020, month 15
    if not 1<=month<=12:
        return'Invalid Month'
    # since year is 2020, a leap year, it returns as true
    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

# For First Function
print(is_leap(2020)) # checks the input year

# For Second Function
print(days_in_month(2020, 2)) # checks the input year and month