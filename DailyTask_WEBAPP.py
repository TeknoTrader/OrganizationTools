#----------------------------------------------------------
#----------------------------------------------------------
#     THIS IS A WEB APP THAT I REALIZED USING STREAMLIT
# With this web app you will be able to organize yourself for exams,
# work projects and all that requires ending a certain task within a
# certain T amount of time.
#----------------------------------------------------------
#----------------------------------------------------------
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import date
import math

# INPUTS

# The day of the exam
st.write("# DETAILS ABOUT THE 📚 EXAM")
st.write("### Let's see when we are going to do it\n### Please, insert the date compiling the following parameters 📅\n")
year = 2024
year1 = st.number_input("Insert the year: ", value = 2024, step=1, min_value=2024)
year = int(year1)   #,value = 2024, step = 1)#value = datetime.today().year)  # Insert the year of the exam
month1 = st.slider("Month: ", 1,12,1)
day1 = st.slider("Day: ", 1,31,1)

ft = date(year,month1,day1)
pages = st.number_input("Number of pages 📖: ", step=1)

# Days left?
td = datetime.date.today()       # Actual datetime
diff = ft - td   # How many days are left for the exam?

st.write("\n")
if(diff.days > 0):   # If there is a POSITIVE amount of days between exams and today
  st.write("# STARTING OF THE OUTPUTS")
  st.write ("\n### Days left ⏰ for the exam:\t",diff.days)                # Days left, output print
  st.write("\n### Average pages 📝 per day:\t",math.ceil(pages/(diff.days-1)))  # Round at the next integer number

  st.write("\n\n\n")
  st.write("# Do you want to have the time to do a review or to relax? 🧘‍♀️")
  st.write("### You calculate how to do that: let's see different scenarios!")

  increment = st.number_input("Interval progression: ", min_value=1,step=1)  # Let's see different scenarios, starting from here
  possibilities = 0
  pages_number = []
  days_number = []
  while diff.days > possibilities:   # Calculating the possible scenarios
    possibilities += increment
    if(diff.days-1-possibilities > 0):   # Avoiding 0 divisions or other common errors
      pages_number.append(round(pages/(diff.days-1-possibilities),1))
      days_number.append(possibilities)
    else:
      break  # End of the cycle in case of 0 division or negative numbers of days
  # Chart creation
  fig, ax = plt.subplots()
  ax.bar(days_number, pages_number)
  ax.set_xlabel('Rest days')
  ax.set_ylabel('Pages per day')
  ax.set_title('Studying possibilities')

  # Visualization
  if (len(days_number) > 1):
    st.pyplot(fig)

  # Comments to clarify
  for i in range(len(days_number)):
    if (len(days_number) > 10):
      st.write(f"\nTo have {i} days off, you should study: {pages_number[i]} pages 📖 per day")
    elif (len(days_number) > 5):
      st.write(f"### \nTo have {i} days off, you should study: {pages_number[i]} pages 📖 per day")
    else:
      st.write(f"# \nTo have {i} days off, you should study: {pages_number[i]} pages 📖 per day")

else:
    st.write("\n")
    st.write("# ⚠️⚠️⚠️ATTENTION⚠️⚠️⚠️")
    st.write("\n")
    st.write("### The exam should be AFTER the actual date!!!")
