import streamlit as st
import requests

st.markdown("""# Are you eligible to borrow?
## Check if you're bankable !! 💵
""")

#age
age_input = int(st.slider('Age', 18, 99, 25))

#incomes
income_input = int(st.number_input('Income'))

#term
term_input = int(st.slider('Term ?', 5, 30, 20) *12)
st.text(f'equal to {term_input} months')

#property value
warranty_input = int(st.number_input('Property value'))

#how much?
expect_input = int(st.number_input('How much do you need'))

#API part
    #request construction
API_URL="https://my-api-app-automated-loan-review-project-qzju5w56rq-ew.a.run.app"
url = f"{API_URL}/predict"

params = {
    'age': age_input,
    'income': income_input,

    #'term':term_input,
    #'warranty':warranty_input,

    'loan_limit': expect_input,

    #'petal_width': petal_width,
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
