# How much should I study/work every day to reach X goal within Y day?
# You an use this program to find it out!

from datetime import date
import math

# INPUTS

# The day of the exam
year = int(input("Year: \t"))
month = int(input("Month: \t"))
day = int(input("Day: \t"))
ft = date(year,month,day)
pages = int(input("Number of pages:\t"))

# Days left?
td = datetime.date.today()       # Actual datetime
diff = ft - td

print("\nSTARTING OF THE OUTPUTS")
print ("\nDays left for the exam:\n\t",diff.days)                # Days left, output print
print("\nAverage pages per day:\n\t",(math.ceil(pages/(diff.days-1))))  # Round at the next integer number

print("\nDo you want to have the time to do a review or to relax?")
print("You could do that")

increment = int(input("Interval progression:\t"))   # Let's see different scenarios, starting from here
possibilities = 0 
while diff.days > possibilities:   # Calculating the possible scenarios
  possibilities += increment
  if(diff.days-1-possibilities >= 0):   # Avoiding 0 divisions or other common errors
   print(f"\nTo have {possibilities} days off, you should study: {(math.ceil(round(pages/(diff.days-1-possibilities))))} pages per day")
  else:
    break  # End of the cycle in case of 0 division or negative numbers of days
