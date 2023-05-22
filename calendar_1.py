def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  # On oluline et see "YEAR, MONTH" on samas järjekorras nagu all
  # rea peal "days = days_in_month(year, month)" sest muidu ta üritab siin panna aasta numbrit
  # kuu koha peale ja kuu numbrit aasta kohapeale. 
  
  # Check if the year is a leap year using the is_leap function
  if month == 2 and is_leap(year):
    return 29
  else:
    # Use a list to store the number of days for each month
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month-1]

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







