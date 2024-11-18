import streamlit as st
import requests
#import base64

#st.image('../raw_data/FROG_BANK.png', caption='',  width=125)

#def load_image(path):
#    with open(path, 'rb') as f:
#        data = f.read()
#    encoded = base64.b64encode(data).decode()
#    return encoded

#path = "../raw_data/FROG_BANK.png"
#encoded = load_image(path)

CSS=f'''
h1 {{
    color: white;
    background-color: #538935;
}}
h2 {{
    color: white;
    background-color: #538935;
}}
.stApp {{
    background-color:#f8f8f8;
    background-image: url("https://github.com/YannAll/automated_loan_review_front_end/blob/e4c4434ee3d68c874b7d6e5ec440b08345bc0a5c/raw_data/FROG_BANK.png?raw=true");
    background-repeat: no-repeat;
    background-position: 90% 10%;
    background-size: 125px 166px;
    }}
'''
#RGV COLOR = 83,137,53

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

st.markdown("""#  Are you eligible to borrow?
## Check if you're bankable !! 💵
""")

#->> Personal informations <<-
st.markdown("""### About you : """)
columns = st.columns(3)

#age
age_input = int(columns[0].slider('Age', 18, 99, 25))

if age_input<25:
    age_input="<25"
elif age_input<35:
    age_input="25-34"
elif age_input<45:
    age_input="35-44"
elif age_input<55:
    age_input="45-54"
elif age_input<65:
    age_input="55-64"
elif age_input<75:
    age_input="65-74"
else:
    age_input=">74"

#incomes
income_input = columns[1].number_input('Annual income', min_value=0, step=5000, format='%d')

open_credit_input= columns[2].radio(
    'Have you ever subscribed to a loan?',
    ['First time', 'I plead guilty !'],
    horizontal=True,
    )
if open_credit_input=='Personal loan':
    open_credit_input='nopc'
else:
    open_credit_input='opc'

#->> Project informations <<-
st.markdown("""### About your project : """)

columns = st.columns(2)

#business_or_commercial
business_or_commercial_input= columns[0].radio(
    'Is it for business or personal use?',
    ['Personal loan', 'Business or commercial loan'],
    label_visibility="collapsed",
    )

if business_or_commercial_input=='Personal loan':
    business_or_commercial_input='nob/c'
else:
    business_or_commercial_input='ob/c'

#property value
property_value_input = int(columns[1].number_input('Property value', min_value=10000, step=5000, format='%d'))

#->> Project informations <<-
st.markdown("""### About the loan : """)
columns = st.columns(2)

#loan_amount
loan_amount_input = int(columns[1].number_input('How much do you need?', min_value=10000, step=5000, format='%d'))

#terms
term_input = int(columns[0].slider('How long do you want to sign up for? (years)', 5, 30, 20) *12)

#API part
    #request construction
API_URL="https://automated-loan-review-project-qzju5w56rq-ew.a.run.app" #"https://my-api-app-automated-loan-review-project-qzju5w56rq-ew.a.run.app"
url = f"{API_URL}/predict"

params = {
    'age': age_input,
    'business_or_commercial' :business_or_commercial_input,
    'income' : income_input,
    'loan_amount' : loan_amount_input,
    #'loan_limit' : loan_amount_input,
    'open_credit' : open_credit_input,
    'property_value' : property_value_input,
    'term' : term_input,
}

img_url_no="https://ih1.redbubble.net/image.1736163822.8931/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg"
img_url_yes="https://ih1.redbubble.net/image.1732971092.0283/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg"


if st.button("Click to discover the best we can do"):

    response = requests.get(url, params=params).json()
    columns = st.columns(2)
    columns[1].markdown(f"**{str(response['status'])}**")

    if response['status'][-15:]=="is not approved":
        columns[0].image(img_url_no,  width=200)

    else:
        columns[1].markdown(f"**at {response['interest_rate']} !!**")
        columns[0].image(img_url_yes,  width=200)
