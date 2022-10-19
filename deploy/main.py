import streamlit as st
import pickle
import json


## Creating the header of our App ##

st.markdown("<h1 style='text-align: center; color: black;'>Vehicle Insurance Fraud Prediction App</h1>", unsafe_allow_html=True)

htp="https://raw.githubusercontent.com/mathlaranjeira/Vehicle-Claim-Fraud-Detection/deploy/car_insurance.png"

col1, col2, col3 = st.columns(3)

with col1:
    st.image(htp, width = 250)

with col2:
    st.image(htp, width = 250)

with col3:
    st.image(htp, width = 250)


# importing the model

model = pickle.load(open('deploy/rf.sav', 'rb'))

# Opening the json files

with open('deploy/vehicle_price_cat_to_number.json', 'r') as file_json:
    vehicle_price_get = json.loads(file_json.read())

with open('deploy/all_perils_cat_to_num.json', 'r') as file_json:
    all_perils_get = json.loads(file_json.read())

with open('deploy/sedan_cat_to_num.json', 'r') as file_json:
    sedan_get = json.loads(file_json.read())

with open('deploy/policy_holder_cat_to_num.json', 'r') as file_json:
    policy_holder_get = json.loads(file_json.read())

with open('deploy/deductible.json', 'r') as file_json:
    deductible_get = json.loads(file_json.read())

with open('deploy/address_change_claim_cat_to_num.json', 'r') as file_json:
    address_change_get = json.loads(file_json.read())

# creating the boxes to select the values of each attribute

st.subheader('Select relevant features of the accident.')

vehicle_price = st.selectbox("Vehicle class price: ", vehicle_price_get.keys())
all_perils = st.selectbox("Was considered all perils? ", all_perils_get.keys())
sedan = st.selectbox("Was the vehicle a Sedan? ", sedan_get.keys())
policy_holder = st.selectbox("Was the person the policy holder? ", policy_holder_get.keys())
deductible = st.selectbox("Select the deductible: ", deductible_get)
address_change = st.selectbox( "Was there an address change recently?: ", address_change_get.keys())
age = st.slider("How old was the driver?", min_value = 16, max_value = 90, step = 1)

####### convert the input as like original data ######

## the numerical values were taken from the box created above, those attributes doesn't need convertion, like Age and Deductible
## for categorical attributes, we use the function .get(), as the variables created above attribute_convert (like deductible_get) 
## are dictionaries, this function will get the value of the correspondent key.

input_all_perils = all_perils_get.get(all_perils)
input_sedan = sedan_get.get(sedan)
input_policy_holder = policy_holder_get.get(policy_holder)
input_deductible = deductible
input_address_change = address_change_get.get(address_change)
input_age = age
input_vehicle_price = vehicle_price_get.get(vehicle_price)

## Crreating the button that will play the model ##

if st.button('Make Fraud Prediction'):

    inputs = [[input_all_perils, input_sedan, input_policy_holder, input_deductible, input_address_change, input_age, input_vehicle_price]]
    prediction = model.predict(inputs)
    if prediction == 0:
        st.markdown("<h1 style='text-align: center; color: black;'>It is not a fraud</h1>", unsafe_allow_html=True)
        
    else: 
        st.markdown("<h1 style='text-align: center; color: black;'>It is a fraud</h1>", unsafe_allow_html=True)
