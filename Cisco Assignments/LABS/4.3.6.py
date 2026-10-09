def is_year_leap(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month < 1 or month > 12 or year < 1:
        return None
    
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2 and is_year_leap(year):
        return 29
        
    return month_days[month]

def day_of_year(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)
    
    total_days += day
    return total_days
print(day_of_year(2000, 12, 31))