import streamlit as st
import datetime

st.markdown("""# Are you eligible to borrow?
## Check if you're bankable !!
""")



# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider


#age
d = st.date_input(
    "Birth date?",
    datetime.date(1988, 1, 1))
#incomes
number = st.number_input('Income')
#term
line_count = st.slider('Term', 1, 25, 3)
#property value
number = st.number_input('Property value')
#how much?
number = st.number_input('How much')
