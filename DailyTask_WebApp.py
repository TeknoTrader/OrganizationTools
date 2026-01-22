import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import date
import math
import calendar

# Sidebar configuration with developer information and resources
st.sidebar.write("# Who built this web application?")
st.sidebar.write("My name is Nicola Chimenti and I am a Business Analyst and MQL4 developer.")
st.sidebar.write("I have a degree in \"Digital Economics\" and I love finance, programming and Data Science.")
st.sidebar.image("https://i.postimg.cc/7LynpkrL/Whats-App-Image-2024-07-27-at-16-36-44.jpg")
st.sidebar.write("\n# CONTACT ME")
st.sidebar.write("### [LinkedIn](https://www.linkedin.com/in/nicolachimenti?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
st.sidebar.write("### [Fiverr profile](https://www.fiverr.com/sellers/teknonicola/) with reviews")
st.sidebar.write("### Email: nicola.chimenti.work@gmail.com")
st.sidebar.write("\n# RESOURCES")
st.sidebar.write("[GitHub Profile](https://github.com/TeknoTrader)")
st.sidebar.write("[MQL5 Profile](https://www.mql5.com/it/users/teknotrader)")
st.sidebar.write("[MT4 free softwares](https://www.mql5.com/it/users/teknotrader/seller#!category=2) for trading")
st.sidebar.write("\n### Are you interested in the source code?")
st.sidebar.write("Visit the [GitHub repository](https://github.com/TeknoTrader/OrganizationTools)")

# Initialize current date
today = datetime.date.today()

# Month names array for user-friendly display
MONTHS = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

# Main application header and description
st.write("# LET'S ORGANIZE YOUR STUDY/WORK!")
st.write("### With this simple and practise web application you can see how much you should work/study to complete a certain task within a certain date")
st.divider()

# Date validation function
def is_valid_date(year, month, day):
    """
    Validates if the selected day exists in the given month and year
    Returns False if valid, True if invalid
    """
    max_days_in_month = calendar.monthrange(year, month)[1]
    return day > max_days_in_month

# User input section for deadline date
st.write("# First step: INSERT DETAILS ABOUT THE EXAM/DEADLINE")
st.write("### Let's see when we are going to do it")
st.write("### Please, insert the date compiling the following parameters")

year = st.number_input("Insert the year: ", min_value=today.year, value=today.year, step=1)
month = st.slider("Month: ", min_value=1, max_value=12, value=today.month, step=1)
day = st.slider("Day: ", min_value=1, max_value=31, value=today.day, step=1)

# Date validation check
if is_valid_date(int(year), int(month), int(day)):
    st.write("\n")
    st.warning("# ATTENTION")
    st.write(f"# The month of {MONTHS[month-1]} has only {calendar.monthrange(int(year), int(month))[1]} days")
    st.write("# Please, select another day.")
else:
    # Workload input
    deadline_date = date(int(year), month, day)
    st.write("### How much do you have to study/work?")
    total_pages = st.number_input("Number of pages/tasks: ", step=1)

    # Calculate days remaining until deadline
    days_difference = deadline_date - today
    days_remaining = days_difference.days

    # Main calculation logic
    st.write("\n")
    if days_remaining > 0 and not is_valid_date(int(year), int(month), int(day)):
        st.write("# STARTING OF THE OUTPUTS")
        st.write(f"### Days left for the exam/deadline: {days_remaining}")
        
        # Calculate daily workload
        if days_remaining > 1:
            daily_workload = math.ceil(total_pages / (days_remaining - 1))
            st.write(f"### Average pages/tasks per day: {daily_workload}")
            st.write("Keep in mind that today is not included in the calculation.")
            st.write("Also, all of the results are approximated: the result you see above was approximated at the next integer number available")
        else:
            st.write(f"### If the deadline is tomorrow, unfortunately this web app can't help you...")
            st.write(f"Average pages/tasks per day: {total_pages}")

        # Advanced planning section with rest days scenarios
        if days_remaining > 2 and total_pages > 0:
            st.divider()
            st.write("# Do you want to have the time to do a review of your work or to relax?")
            st.write("### You calculate how to do that: let's see different scenarios!")

            # Scenario calculation inputs
            increment = st.number_input("Interval progression: ", min_value=1, step=1)
            decimal_precision = st.number_input("Decimal approximation: ", value=1, min_value=0, step=1)

            # Arrays for storing calculation results
            pages_per_day_list = []
            rest_days_list = []
            
            # Calculate scenarios with progressive rest days
            scenarios_counter = 0
            while days_remaining > scenarios_counter:
                scenarios_counter += increment
                working_days = days_remaining - 1 - scenarios_counter
                
                if working_days > 0:
                    pages_per_day = round(total_pages / working_days, decimal_precision)
                    pages_per_day_list.append(pages_per_day)
                    rest_days_list.append(scenarios_counter)
                else:
                    break

            # Generate bar chart for scenarios visualization
            if len(rest_days_list) > 1:
                fig, ax = plt.subplots()
                ax.bar(rest_days_list, pages_per_day_list)
                ax.set_xlabel('Rest days')
                ax.set_ylabel('Pages/tasks per day')
                ax.set_title('Possible organization strategies')
                st.pyplot(fig)

            # Create dataframe for detailed table view
            scenario_data = {
                'Days Off': [(1 + i) * increment for i in range(len(rest_days_list))],
                'Pages/Tasks per Day': pages_per_day_list
            }
            df_scenarios = pd.DataFrame(scenario_data)

            # Display results based on number of scenarios
            st.write("## Roadmap in details")
            if len(rest_days_list) < 5:
                for i in range(len(rest_days_list)):
                    header_level = "###" if len(rest_days_list) > 3 else "#"
                    st.write(f"{header_level} To have {(1 + i) * increment} days off, you should study/do: {pages_per_day_list[i]} pages/tasks per day")
            else:
                # Radio button for table display format selection
                display_format = st.radio(
                    "### Type of table:",
                    ["Normal (you can also download the dataframe as CSV file)", 
                     "Extended (better for decimals numbers visualization)"]
                )
                
                if display_format == "Normal (you can also download the dataframe as CSV file)":
                    st.dataframe(df_scenarios, hide_index=True)
                else:
                    # Extended table view with custom CSS styling
                    table_data = pd.DataFrame({
                        'Days Off you can get': [(1 + i) * increment for i in range(len(rest_days_list))],
                        'Pages/Tasks per Day': pages_per_day_list
                    })
                    
                    # CSS for hiding table index
                    hide_index_css = """
                        <style>
                        thead tr th:first-child {display:none}
                        tbody th {display:none}
                        </style>
                    """
                    st.markdown(hide_index_css, unsafe_allow_html=True)
                    
                    # Display styled table with bar visualization
                    st.table(table_data.style.format(
                        subset=['Pages/Tasks per Day'],
                        decimal=',',
                        precision=decimal_precision
                    ).bar(subset=['Pages/Tasks per Day'], align="mid"))

    # Error handling for invalid date selection
    else:
        st.write("\n")
        st.warning("# ATTENTION")
        st.write("### The exam/deadline should be AFTER the actual date!")

    # Error handling for zero workload
    if total_pages == 0:
        st.write("\n")
        st.warning("# ATTENTION")
        st.write("### Insert the number of pages/hours!")
