import pandas as pd
import numpy as np
import streamlit as st
import warnings
warnings.filterwarnings('ignore')
from datetime import datetime
import pickle
import sklearn

def town_mapping(town_map):
    if town_map == 'ANG MO KIO':
        town_1 = int(0)
    elif town_map == 'BEDOK':
        town_1 = int(1)
    elif town_map == 'BISHAN':
        town_1 = int(2)
    elif town_map == 'BUKIT BATOK':
        town_1 = int(3)
    elif town_map == 'BUKIT MERAH':
        town_1 = int(4)
    elif town_map == 'BUKIT TIMAH':
        town_1 = int(6)
    elif town_map == 'CENTRAL AREA':
        town_1 = int(7)
    elif town_map == 'CHOA CHU KANG':
        town_1 = int(8)
    elif town_map == 'CLEMENTI':
        town_1 = int(9)
    elif town_map == 'GEYLANG':
        town_1 = int(10)
    elif town_map == 'HOUGANG':
        town_1 = int(11)
    elif town_map == 'JURONG EAST':
        town_1 = int(12)
    elif town_map == 'JURONG WEST':
        town_1 = int(13)
    elif town_map == 'KALLANG/WHAMPOA':
        town_1 = int(14)
    elif town_map == 'MARINE PARADE':
        town_1 = int(16)
    elif town_map == 'QUEENSTOWN':
        town_1 = int(19)
    elif town_map == 'SENGKANG':
        town_1 = int(21)
    elif town_map == 'SERANGOON':
        town_1 = int(22)
    elif town_map == 'TAMPINES':
        town_1 = int(23)
    elif town_map == 'TOA PAYOH':
        town_1 = int(24)
    elif town_map == 'WOODLANDS':
        town_1 = int(25)
    elif town_map == 'YISHUN':
        town_1 = int(26)
    elif town_map == 'LIM CHU KANG':
        town_1 = int(15)
    elif town_map == 'SEMBAWANG':
        town_1 = int(20)
    elif town_map == 'BUKIT PANJANG':
        town_1 = int(5)
    elif town_map == 'PASIR RIS':
        town_1 = int(17)
    elif town_map == 'PUNGGOL':
        town_1 = int(8)

    return town_1

def flat_type_mapping(flat_type):
    if flat_type == '1 ROOM':
        flat_1 = int(0)
    elif flat_type == '3 ROOM':
        flat_1 = int(2)
    elif flat_type == '4 ROOM':
        flat_1 = int(3)
    elif flat_type == '5 ROOM':
        flat_1 = int(4)
    elif flat_type == '2 ROOM':
        flat_1 = int(1)
    elif flat_type == 'EXECUTIVE':
        flat_1 = int(5)
    elif flat_type == 'MULTI GENERATION':
        flat_1 = int(6)
    
    return flat_1

def flat_model_mapping(flat_model):
    if flat_model == 'improved':
        flat_model = int(5)
    elif flat_model == 'new generation':
        flat_model = int(12)
    elif flat_model == 'model a':
        flat_model = int(8)
    elif flat_model == 'standard':
        flat_model = int(17)
    elif flat_model == 'simplified':
        flat_model = int(16)
    elif flat_model == 'model a maisonette':
        flat_model = int(9)
    elif flat_model == 'apartment':
        flat_model = int(3)
    elif flat_model == 'maisonette':
        flat_model = int(7)
    elif flat_model == 'terrace':
        flat_model = int(18)
    elif flat_model == '2 room':
        flat_model = int(0)
    elif flat_model == 'improved maisonette':
        flat_model = int(6)
    elif flat_model == 'multi generation':
        flat_model = int(11)
    elif flat_model == 'premium apartment':
        flat_model = int(13)
    elif flat_model == 'adjoined flat':
        flat_model = int(2)
    elif flat_model == 'premium maisonette':
        flat_model = int(15)
    elif flat_model == 'model a2':
        flat_model = int(10)
    elif flat_model == 'type s1':
        flat_model = int(19)
    elif flat_model == 'type s2':
        flat_model = int(20)
    elif flat_model == 'dbss':
        flat_model = int(4)
    elif flat_model == 'premium apartment loft':
        flat_model = int(14)
    elif flat_model == '3gen':
        flat_model = int(1)

    return flat_model

def predict_price (year,town,flat_type,flat_model,floor_area_sqm,lease_commence_date,storey_start,storey_end):

    year_pp = int(year)
    town_pp = town_mapping(town)
    flat_type_pp = flat_type_mapping(flat_type)
    flat_model_pp = flat_model_mapping(flat_model)
    floor_area_sqm_pp = int(floor_area_sqm)
    lease_commence_date_pp = int(lease_commence_date)
    storey_start_pp = np.log(int(storey_start))
    storey_end_pp = np.log(int(storey_end))

    with open (r'singapore_flat_resale_model.pkl','rb') as f:
        regg_mod = pickle.load(f)
        
    user_data = np.array([[year_pp,town_pp,flat_type_pp,flat_model_pp,floor_area_sqm_pp,
                           lease_commence_date_pp,storey_start_pp,storey_end_pp]])
    y_pred = regg_mod.predict(user_data)
    price = np.exp(y_pred[0])

    return round(price)


st.set_page_config(layout='wide')

st.title ("Singapore Resale Flats Price Prediction")
st.write(" ")

tab1,tab2 = st.tabs(['About','Price Prediction'])

with tab1:
    st.header('Real Estate in Singapore:')
    st.write("Singapore's real estate market is projected to grow steadily, with an estimated market size of **USD 49.64 billion in 2025**, reaching **USD 68.24 billion by 2030**.")
    st.write("The rental market has been stabilizing, with rental increases slowing down over time.") 
    st.write("Government initiatives continue to support affordable housing, ensuring high homeownership rates while influencing overall property prices.") 
    st.write("The office sector is evolving, with companies shifting beyond the traditional city center to accommodate new workplace preferences.")
    st.header('Resale Flats:')
    st.write("In Singapore, mature estates like Toa Payoh and Queenstown, tend to see higher resale prices due to their amenities and accessibility, while non-mature estates offer more budget-friendly options. ")
    st.write("Buyers often consider flat size, lease remaining, and nearby MRT stations when making their decisions. There’s also growing interest in million-dollar flats, particularly larger units in prime locations.")

with tab2:

    date_options = list(range(1990,2026))
    date_options_1 = list(range(1966,2021))

    col1,col2 = st.columns(2)

    with col1:
        
        year = st.selectbox("Select The Year",date_options)

        town = st.selectbox("Select The Town",['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                                                'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI',
                                                'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                                                'KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'SENGKANG',
                                                'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN',
                                                'LIM CHU KANG', 'SEMBAWANG', 'BUKIT PANJANG', 'PASIR RIS',
                                                'PUNGGOL'])
        
        flat_type = st.selectbox("Select The Flat Type",['1 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE',
                                                        'MULTI GENERATION'])
        
        flat_model = st.selectbox("Select The Flat Model",['improved', 'new generation', 'model a', 'standard', 'simplified',
                                                            'model a maisonette', 'apartment', 'maisonette', 'terrace',
                                                            '2 room', 'improved maisonette', 'multi generation',
                                                            'premium apartment', 'adjoined flat', 'premium maisonette',
                                                            'model a2', 'type s1', 'type s2', 'dbss', 'premium apartment loft',
                                                            '3gen'])

    with col2:

        floor_area_sqm = st.number_input("Enter The Floor Area (Min: 28 / Max: 366)")

        lease_commence_date = st.selectbox("Select The Lease Commence Date",date_options_1)
        
        storey_start = st.number_input("Enter The Storey Start Value (Min: 1 / Max: 49) ")

        storey_end = st.number_input("Enter The Storey End Value (Min: 3 / Max: 51)")


    button = st.button("Predict The Price",use_container_width=True)

    if button:

        price = predict_price(year,town,flat_type,flat_model,floor_area_sqm,lease_commence_date,storey_start,storey_end)

        st.write ("**The Predicted Price is:**",price)


        



                                                                
        