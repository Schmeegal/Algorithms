
#excercise in steps of problem solving
#not very fast - better to use datetime built in to python

days_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def next_day(y, m, d):
    if d < day_in_month(y, m):
        return y, m, d+1
    else:
        if m < 12:
            return y, m + 1, 1
        else:
            return y + 1, 1, 1

def date_is_before(y1, m1, d1, y2, m2, d2):
    if y1 < y2:
        return True
    if y1 == y2:
        if m1 < m2:
            return True
        if m1 == m2:
            return d1 < d2
    return False

def day_in_month(y, m):
    days = days_of_month[m-1]
    if days == 28:
        if is_leap_year(y):
            days = 29
    return days

def days_between_dates(y1, m1, d1, y2, m2, d2): #birhtdate and today's date
    days = 0
    while date_is_before(y1, m1, d1, y2, m2, d2):
        y1, m1, d1 = next_day(y1, m1, d1)
        days += 1
    return days

    # if y1==y2 and m1==m2 and d1==d2:
    #     return "0 days old"
    # elif y1<y2 or (y1==y2 and m1<m2) or (y1 == y2 and m1==m2 and d1<d2):
    #     return "Invalid input. Birthdate must come before today's date."
    #start with birthday
    #check if leap year
    #m = m-1 in days_of_month
    #check how many days left in month of m1
    #for each year, iterate through months and add together


def test():
    assert days_between_dates(2013, 1, 1, 2013, 1, 1) == 0
    assert days_between_dates(2013, 1, 1, 2013, 1, 2) == 1
    assert next_day(2013, 1, 1) == (2013, 1, 2)
    assert next_day(2013, 4, 30) == (2013, 5, 1)
    assert next_day(2012, 12, 31) == (2013, 1, 1)
    assert next_day(2013, 2, 28) == (2013, 3, 1)
    assert next_day(2013, 1, 30) == (2013, 1, 31)
    assert days_between_dates(2012, 1, 1, 2013, 1, 1) == 366
    assert days_between_dates(2013, 1, 1, 2014, 1, 1) == 365
    print("Test finished")

test()

print(is_leap_year(2012))