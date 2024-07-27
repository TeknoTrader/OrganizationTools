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

# Description of the program
st.write("# LET'S ORGANIZE YOUR STUDY/WORK! 🏃")
st.write("### With this simple and practise web application you can see how much you should work/study to complete a certain task within a certain date")
# INPUTS
# The day of the exam
st.write("# First step: INSERT DETAILS ABOUT THE 📚 EXAM/DEADLINE")
st.write("### Let's see when we are going to do it\n### Please, insert the date compiling the following parameters 📅\n")
year = 2024
year1 = st.number_input("Insert the year: ", value = 2024, step=1, min_value=2024)
year = int(year1)   #,value = 2024, step = 1)#value = datetime.today().year)  # Insert the year of the exam
month1 = st.slider("Month: ", 1,12,1)
day1 = st.slider("Day: ", 1,31,1)

ft = date(year,month1,day1)
st.write("### How much do you have to study/work 📖?")
pages = st.number_input("Number of pages/tasks: ", step=1)

# Days left?
td = datetime.date.today()       # Actual datetime
diff = ft - td   # How many days are left for the exam?

st.write("\n")
if(diff.days > 0):   # If there is a POSITIVE amount of days between exams and today
  st.write("# STARTING OF THE OUTPUTS")
  st.write ("\n### Days left ⏰ for the exam/deadline:\t",diff.days)                # Days left, output print
  if (diff.days > 1):
    st.write("\n### Average pages/tasks 📝 per day:\t",math.ceil(pages/(diff.days-1)))  # Round at the next integer number
    st.write("\n### Today is not included in the calculation")
  else:
    st.write("\n### If the deadline is tomorrow, unfortunately this web app can't help you...\nAverage pages/tasks 📝 per day:\t",pages) # Only one day to finish all...

  if (diff.days > 2):
    st.write("\n\n\n")
    st.write("# Do you want to have the time to do a review of your work or to relax? 🧘‍♀️")
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
    ax.set_ylabel('Pages/tasks per day')
    ax.set_title('Possible organizations strategies')

    # Visualization
    if (len(days_number) > 1):
      st.pyplot(fig)

    # Comments to clarify
    for i in range(len(days_number)):
      if (len(days_number) > 10):
        st.write(f"\nTo have {(1+i) * increment} days off, you should study/do: {pages_number[i]} pages/tasks 👩🏻‍💻 per day")
      elif (len(days_number) > 5):
        st.write("\n### To have ", (1+i) * increment, " days off, you should study/do: ", pages_number[i], " pages/tasks 👩🏻‍💻 per day")
      else:
        st.write("\n# To have ", (1+i) * increment, " days off, you should study/do: ", pages_number[i], " pages/tasks 👩🏻‍💻 per day")

else:
    st.write("\n")
    st.write("# ⚠️⚠️⚠️ATTENTION⚠️⚠️⚠️")
    st.write("\n")
    st.write("### The exam should be AFTER the actual date!!!")
