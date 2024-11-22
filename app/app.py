import streamlit as st
import requests

st.set_page_config(
    page_title="Frog Bank",
    page_icon=":frog:",
    layout="wide",
    #initial_sidebar_state="collapsed",
)
st.logo(
    "https://github.com/YannAll/automated_loan_review_front_end/blob/main/raw_data/FB_LOGO.png?raw=true",
    link="https://github.com/YannAll/automated_loan_review_front_end",
    icon_image="https://github.com/YannAll/automated_loan_review_front_end/blob/main/raw_data/FB_LOGO.png?raw=true",
)

CSS='''
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');
html, body, h1, h2, h3,  [class*="css"]  {
    font-family: 'Playfair Display', serif;
}

.stApp {
    background-color:white;
    background-image: url("https://github.com/YannAll/automated_loan_review_front_end/blob/main/raw_data/FB_LOGO.png?raw=true");
    background-repeat: no-repeat;
    background-position: 90% 12.5%;
    background-size: 231px 200px;
    font-family: 'Playfair Display', serif;
    }
'''
st.markdown(f'<style>{CSS}</style>', unsafe_allow_html=True)

st.markdown("""# Are you eligible to borrow?
## Check if you're bankable !! 💵
""")

#->> Personal informations <<-
st.markdown("""### About you : """)
columns = st.columns(2)

name_input=columns[0].text_input("Name")

#age
age_input = int(columns[1].slider('Age', 18, 99, 25))

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
income_input = columns[0].number_input('Annual income', min_value=0, step=5000, format='%d')

open_credit_input= columns[1].radio(
    'Have you ever subscribed to a loan?',
    ['First time', 'I plead guilty !'],
    horizontal=True,
    #label_visibility="collapsed"
    )
if open_credit_input=='Personal loan':
    open_credit_input='nopc'
else:
    open_credit_input='opc'

#->> Project informations <<-
st.markdown("""### About your project : """)

columns = st.columns(2)
#property value
property_value_input = int(columns[0].number_input('Property value', min_value=5000, step=5000, format='%d'))

#business_or_commercial
business_or_commercial_input= columns[1].radio(
    'Is it for business or personal use?',
    ['Personal loan', 'Business or commercial loan'],
    horizontal=True,
    label_visibility="hidden",
    #"hidden" #collapsed
    )

if business_or_commercial_input=='Personal loan':
    business_or_commercial_input='nob/c'
else:
    business_or_commercial_input='ob/c'

#->> Project informations <<-
st.markdown("""### About the loan : """)
columns = st.columns(2)

#loan_amount
loan_amount_input = int(columns[0].number_input('How much do you need?', min_value=10000, step=5000, format='%d'))

#terms
term_input = int(columns[1].slider('How long do you want to sign up for? (years)', 5, 30, 20) *12)

#API part
    #request construction
API_URL="https://automated-loan-review-project-qzju5w56rq-ew.a.run.app" #"https://my-api-app-automated-loan-review-project-qzju5w56rq-ew.a.run.app"
url = f"{API_URL}/predict"

params = {
    'age': age_input,
    'business_or_commercial' :business_or_commercial_input,
    'income' : income_input,
    'loan_amount' : loan_amount_input,
    'open_credit' : open_credit_input,
    'property_value' : property_value_input,
    'term' : term_input,
}

#img_url_no="https://ih1.redbubble.net/image.1736163822.8931/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg"
img_url_no="https://i.pinimg.com/originals/2c/80/d2/2c80d2ced9451189047bc6f0c8a54852.gif"
#img_url_yes="https://ih1.redbubble.net/image.1732971092.0283/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg"
img_url_yes="https://cdn.pixabay.com/animation/2023/05/08/06/04/06-04-27-290_512.gif"
columns = st.columns(4)
if columns[1].button("Click to discover the best we can do !"):

    response = requests.get(url, params=params).json()
    #columns = st.columns(2)

    if response['status'][-15:]=="is not approved":
        columns[2].markdown(f"**Unfortunately {name_input} ❌**")
        columns[2].markdown(f"**{str(response['status'])}**")
        columns[3].image(img_url_no,  width=200)

    else:
        columns[2].markdown(f"**Great news {name_input} 🎉**")
        columns[2].markdown(f"**{str(response['status'])} at {response['interest_rate']} !!**")
        columns[3].image(img_url_yes,  width=200)
        #st.markdown(f'<style>{CSS}{CSS2}</style>', unsafe_allow_html=True)




#https://i.pinimg.com/originals/4d/68/cd/4d68cd156b67ed38303691834e7a9628.gif
