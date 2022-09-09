# Python program to demonstrate working of formatmonth() method

# importing calendar module
import calendar

text_cal = calendar.HTMLCalendar(firstweekday=0)

year = 2018
month = 9
# default value of width is 0

# printing formatmonth
print(text_cal.formatmonth(year, month))