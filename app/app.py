import streamlit as st
import requests

st.markdown("""# Are you eligible to borrow?
## Check if you're bankable !! 💵
""")

#->> Personal informations <<-
st.markdown("""### About you : """)

#age
age_input = int(st.slider('Age', 18, 99, 25))

#Gender
gender_input= st.radio('Gender', ('Sex Not Available', 'Female', 'Male', 'Joint'))

#incomes
income_input = int(st.number_input('Income'))

#open credit
if st.checkbox('Any open credit?'):
    st.text('Yes')
    open_credit_input='opc'
else:
    st.text('No')
    open_credit_input='nopc'

#region
region_input= st.radio('Region', ('south', 'North', 'central',  'North-East'))

#->> Project informations <<-
st.markdown("""### About your project : """)

#business_or_commercial
if st.checkbox('Business credit?'):
    st.text('Business or commercial loan')
    business_or_commercial_input='ob/c'
else:
    st.text('Personal loan')
    business_or_commercial_input='nob/c'

#construction_type
construction_type_input= st.radio('Construction type', ('Site built', 'Land to construct'))
if construction_type_input == 'Site built':
    construction_type_input ='sb'
    Secured_by_input='home'
    Security_Type_input='direct'
else:
    construction_type_input ='mh'
    Secured_by_input='land'
    Security_Type_input='Indirect'


#credit type
    # /!\ stand  by

#interest only
interest_only_input= st.radio('Monthly payment', ('In fine loan', 'Amortizing Loan'))
if interest_only_input=="In fine loan":
    st.text('You pay only interest every month and the principal is repaid at the end')
    interest_only_input='int_only'
else:
    st.text('You repaid monthly the principal with interest')
    interest_only_input='not_int'


#loan_amount
loan_amount_input = int(st.number_input('How much do you need'))

#lump_sum_payment
if st.checkbox('Ok with lump sum concept ?'):
    st.text('''Let's go, money is not a problem at this stage''')
    lump_sum_payment_input='lpsm'
else:
    st.text('No way, not a cent more')
    lump_sum_payment_input='not_lpsm'

#occupancy_type
occupancy_type_input= st.radio('Occupancy type', ('primary residence', 'secondary residence','investment property'))
if occupancy_type_input == 'primary residence':
    occupancy_type_input = "pr"
elif occupancy_type_input == 'secondary residence':
   occupancy_type_input="sr"
elif occupancy_type_input =="investment property":
    occupancy_type_input="ir"


#property value
property_value_input = int(st.number_input('Property value'))

#terms
term_input = int(st.slider('Term ?', 5, 30, 20) *12)
st.text(f'equal to {term_input} months')

#total_units
total_units_input = st.slider('Number of property being financed', 1, 4, 1)
total_units_input =f'{total_units_input}U'


#API part
    #request construction
API_URL="https://my-api-app-automated-loan-review-project-qzju5w56rq-ew.a.run.app"
url = f"{API_URL}/predict"

params = {
    'age': age_input,
    #'business_or_commercial' :business_or_commercial_input,
    #'construction_type': construction_type_input,
    #'credit_type' : ??
    #'Gender' : gender_input,
    'income' : income_input,
    #'interest_only' : interest_only_input,
    'loan_limit' : loan_amount_input,
    #'lump_sum_payment':lump_sum_payment_input,
    #'occupancy_type':occupancy_type_input,
    #'open_credit' : open_credit_input,
    #'property_value' : property_value_input,
    #'Region' : region_input,
    #'Secured_by' : Secured_by_input,
    #'Security_Type' : Security_Type_input,
    #'term' : term_input,
    #'total_units' : total_units_input,
}

img_url_no="https://ih1.redbubble.net/image.1736163822.8931/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg"
img_url_yes="https://ih1.redbubble.net/image.1732971092.0283/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg"

response = requests.get(url, params=params).json()
if st.button("Best we can do"):
    st.markdown(f"**{str(response['prediction'])}**")

    if response['prediction'][-15:]=="is not approved":
        st.image(img_url_no,  width=200)

    else:
        st.image(img_url_yes,  width=200)
