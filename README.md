# Singapore Resale Flat Price Prediction  

## Overview  
This project aims to develop a machine learning model to predict the resale price of **HDB flats** in Singapore using historical data spanning **1990 to 2025**. The model is integrated into a **Streamlit application**, allowing users to select relevant features for price prediction.  

## Data Preprocessing  
Before training the model, several preprocessing steps were performed:  
- **Handling skewness** in the dataset  
- **Outlier treatment** using the **Interquartile Range (IQR)** method  
- **Feature engineering** to ensure optimal input variables for the model  

## Model Selection  
After testing various models, **Random Forest** emerged as the most suitable choice due to its **high accuracy (~98%)** and ability to handle complex relationships within the data.  

## Streamlit Application  
The model is deployed through a **Streamlit-based UI**, allowing users to input the following parameters:  
- **Year**  
- **Town**  
- **Flat Type**  
- **Flat Model**  

The selected inputs feed the model, generating a **predicted resale price** for the user.  

## Installation & Usage  
To run the application, follow these steps:  
1. Clone the repository  
2. Install dependencies
4. Run the Streamlit app

If you have any queires, Kindy reach out to me alisafath@gmail.com
