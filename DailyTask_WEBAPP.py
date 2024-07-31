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
import calendar

# Some information about me
st.sidebar.write("# Who built this web application?")
st.sidebar.write("My name is Nicola Chimenti.\nI'm currently pursuing a degree in \"Digital Economics\" and I love finance, programming and Data Science")
st.sidebar.image("https://i.postimg.cc/7LynpkrL/Whats-App-Image-2024-07-27-at-16-36-44.jpg") # caption="My name is Nicola Chimenti.\nI'm currently pursuing a degree in \"Digital Economics\" and I love finance, programming and Data Science" , use_column_width=True)
st.sidebar.write("\n# CONTACT ME")
st.sidebar.write("### ◾ [LinkedIn](https://www.linkedin.com/in/nicolachimenti?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
st.sidebar.write("### ◾ Email: nicola.chimenti.work@gmail.com")
# st.sidebar.write("### ◾ [Fiverr](https://www.fiverr.com/teknonicola?public_mode=true)")
st.sidebar.write("\n# RESOURCES")
st.sidebar.write("◾ [GitHub Profile](https://github.com/TeknoTrader)")
st.sidebar.write("◾ [MQL5 Profile](https://www.mql5.com/it/users/teknotrader) with reviews")
st.sidebar.write("◾ [MT4 free softwares](https://www.mql5.com/it/users/teknotrader/seller#!category=2) for trading")
st.sidebar.write("\n### Are you interested in the source code? 🧾")
st.sidebar.write("Visit the [GitHub repository](https://github.com/TeknoTrader/OrganizationTools)")

td = datetime.date.today()       # Actual datetime

# Description of the program
st.write("# LET'S ORGANIZE YOUR STUDY/WORK! 🏃")
st.write("### With this simple and practise web application you can see how much you should work/study to complete a certain task within a certain date")
# INPUTS
# The day of the exam
st.write("# First step: INSERT DETAILS ABOUT THE 📚 EXAM/DEADLINE")
st.write("### Let's see when we are going to do it\n### Please, insert the date compiling the following parameters 📅\n")
year = 2024
year1 = st.number_input("Insert the year: ", min_value = td.year, value = td.year, step=1)
year = int(year1)   #,value = 2024, step = 1)#value = datetime.today().year)  # Insert the year of the exam
month1 = st.slider("Month: ", min_value=1, max_value=12, value = td.month, step=1)
day1 = st.slider("Day: ", min_value=1, max_value = 31, value = td.day, step=1)

months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

def time_issue():
          if(calendar.monthrange(year1, int(month1))[1] < int(day1)):
                    return True
          else:
                    return False
                    
if (time_issue()):
          st.write("\n")
          st.warning("# ⚠️ATTENTION⚠️\n")
          st.write("# The month of", months[month1], "has only", calendar.monthrange(year1, int(month1))[1], "day...\n\n# Please, select another day.")

else:
          ft = date(year,month1,day1)
          st.write("### How much do you have to study/work 📖?")
          pages = st.number_input("Number of pages/tasks: ", step=1)

          # Days left?
          diff = ft - td   # How many days are left for the exam?

          st.write("\n")
          if(diff.days > 0) and (time_issue() == False):   # If there is a POSITIVE amount of days between exams and today
            st.write("# STARTING OF THE OUTPUTS")
            st.write ("\n### Days left ⏰ for the exam/deadline:\t",diff.days)                # Days left, output print
            if (diff.days > 1):
              st.write("\n### Average pages/tasks 📝 per day:\t",math.ceil(pages/(diff.days-1)))  # Round at the next integer number
              st.write("\n Keep in mind that today is not included in the calculation.")
              st.write("Also, all of the results are approximated: the result you see above was approximated at the next integer number avaible")
    
            else:
              st.write("\n### If the deadline is tomorrow, unfortunately this web app can't help you...\nAverage pages/tasks 📝 per day:\t",pages) # Only one day to finish all...

            if (diff.days > 2) and (pages > 0) and (time_issue() == False):
              st.write("\n\n\n")
              st.write("# Do you want to have the time to do a review of your work or to relax? 🧘‍♀️")
              st.write("### You calculate how to do that: let's see different scenarios!")

              increment = st.number_input("Interval progression: ", min_value=1,step=1)  # Let's see different scenarios, starting from here
              decimal = st.number_input("Decimal approximation: ", value=1, min_value=0, step=1)
              possibilities = 0
              pages_number = []
              days_number = []
              while diff.days > possibilities:   # Calculating the possible scenarios
                possibilities += increment
                if(diff.days-1-possibilities > 0):   # Avoiding 0 divisions or other common errors
                  pages_number.append(round(pages/(diff.days-1-possibilities),decimal))
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

              # Table vaues
              data = {
                  'Days Off 🏖️': [(1+i) * increment for i in range(len(days_number))],
                  'Pages/Tasks per Day 👩🏻‍💻': pages_number
              }

              # Dataframe creation for the table
              df = pd.DataFrame(data)
    
              # Streamlit table or comments
              st.write("## Roadmap in details")
              if (len(days_number) < 5):
                for i in range(len(days_number)):
                  if (len(days_number) > 3):
                    st.write("\n### To have ", (1+i) * increment, " days off, you should study/do: ", pages_number[i], " pages/tasks 👩🏻‍💻 per day")
                  else:
                    st.write("\n# To have ", (1+i) * increment, " days off, you should study/do: ", pages_number[i], " pages/tasks 👩🏻‍💻 per day")
              else: 
                # you can also use st.dataframe(df) or st.table(df)
                rad = st.radio(
                          "### Type of table:",
                          ["Normal (you can also downoad the dataframe)","Extended (better for decimals numbers visualization)"]
                )
                if rad == "Normal (you can also downoad the dataframe)":
                          st.dataframe(df, hide_index=True)  #another way to hide column: st.dataframe(df.set_index(df.columns[0]))
                else:
                          # CSS to inject contained in a string
                          hide_table_row_index = """
                                      <style>
                                      thead tr th:first-child {display:none}
                                      tbody th {display:none}
                                      </style>
                                      """

                          # Inject CSS with Markdown
                          st.markdown(hide_table_row_index, unsafe_allow_html=True)
                          st.table(table1.style.format(subset=['Pages/Tasks per Day 👩🏻‍💻'],
                                                       decimal=',', precision=decimal).bar(subset=['Pages/Tasks per Day 👩🏻‍💻'], align="mid"))
                          df.style.format(precision=0)
                          st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
                          df = pd.DataFrame(data).astype(float)
                          #df = df.style.format(precision=0)
                          
                          
      
          else:
              st.write("\n")
              st.warning("# ⚠️ATTENTION⚠️\n\n### The exam/deadline should be AFTER the actual date!!!")

          if pages == 0:
              st.write("\n")
              st.warning("# ⚠️ATTENTION⚠️\n\n### Insert the number of pages/hours!!!")

   
