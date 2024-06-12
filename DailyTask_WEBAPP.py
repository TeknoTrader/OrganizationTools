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

import datetime
from datetime import date
import math

# INPUTS

# The day of the exam
st.write("# DETAILS ABOUT THE EXAM")
year = 2024
year1 = st.number_input("Insert the year: ", value = 2024, step=1, min_value=2024)
year = int(year1)   #,value = 2024, step = 1)#value = datetime.today().year)  # Insert the year of the exam
month1 = st.slider("Month: ", 1,12,1)
day1 = st.slider("Day: ", 1,31,1)

ft = date(year,month1,day1)
pages = st.number_input("Number of pages: ", step=1)

# Days left?
td = datetime.date.today()       # Actual datetime
diff = ft - td   # How many days are left for the exam?

st.write("\n")
if(diff.days > 0):   # If there is a POSITIVE amount of days between exams and today
  st.write("# STARTING OF THE OUTPUTS")
  st.write ("\n### Days left for the exam:\t",diff.days)                # Days left, output print
  st.write("\n### Average pages per day:\t",math.ceil(pages/(diff.days-1)))  # Round at the next integer number

  st.write("\n\n\n")
  st.write("# Do you want to have the time to do a review or to relax?")
  st.write("### You calculate how to do that: let's see different scenarios!")

  increment = st.number_input("Interval progression: ", min_value=1,step=1)  # Let's see different scenarios, starting from here
  possibilities = 0
  while diff.days > possibilities:   # Calculating the possible scenarios
    possibilities += increment
    if(diff.days-1-possibilities > 0):   # Avoiding 0 divisions or other common errors
      st.write(f"\nTo have {possibilities} days off, you should study: {round(pages/(diff.days-1-possibilities),1)} pages per day")
    else:
      break  # End of the cycle in case of 0 division or negative numbers of days

else:
    st.write("\n")
    st.write("# ATTENTION!!!")
    st.write("\n")
    st.write("### The exam should be AFTER the actual date!")
