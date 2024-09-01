# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#
st.title("Data Analysis")
st.header("Data Analysis Using Python & Streamlit")

# upload dataset
upload = st.file_uploader("Upload Your Dataset (IN CSV FORMAT)")
if upload is not None:
    data = pd.read_csv(upload)

# show database
if st.checkbox("Preview Database"):
    if st.button("Head"):
        st.write(data.head())
    if st.button("Tail"):
        st.write(data.tail())


# check datatype of each column
if upload is not None:
    if st.checkbox("Datatype of Each column"):
        st.text("DataTypes")
        st.write(data.dtypes)


# Find Shape of dataset
if upload is not None:
    data_shape = st.radio(
        "What dimension Do you want to Check?", ('Rows', 'Columns'))
    if data_shape == 'Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape == 'Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])


# Find null values
if upload is not None:
    test = data.isnull().values.any()
    if test:
        if st.checkbox("Null Values in Dataset"):
            # Create a heatmap of null values
            fig, ax = plt.subplots()
            sns.heatmap(data.isnull(), cbar=False, cmap='viridis', ax=ax)
            st.pyplot(fig)
    else:
        st.success("Congratulations!!! No Missing Values In Dataset")
        
#Find the duplicate values in Dataset
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Data Contains Some Duplicate Values")
        dup=st.selectbox("Do you want to remove Duplicate Values?",("Select One","Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values Are Removed")
        if dup=="No":
            st.text("OK NO Problem")
            
# Get Overall Stats
if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe(include="all"))
        
        
# about section
if st.button("About App"):
    st.text("Built with Streamlit")
    st.text("Thanks to Streamlit")
    
#by

if st.checkbox("By"):
    st.success("Shivam Sharma")