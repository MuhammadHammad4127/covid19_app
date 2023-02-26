#importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
header=st.container()
dataset=st.container()
features=st.container()
modelTraining=st.container()
# st.header("USA Covid-19 Data Analysis")
with header:
    st.header(" USA Covid-19 Data Analysis")
    st.text("This is the data analysis of USA Covid-19 of 2020 from March to December")
#reading the dataset
with dataset:
    st.header(" Original Dataset")
df=pd.read_excel("Book1.xlsx")
st.write(df.head(5))
#making sidebars
with features:
    st.sidebar.header("User Input Features")

with modelTraining:
    #  st.header("Predicted Dataset")
    #  st.text("This is the predicted dataset")
    #st.write(df.head(5))
    st.subheader("Predicted Dataset")
# Show total cases by State
st.subheader("Total Deaths in this State")
State_name = st.sidebar.selectbox("Select a State", df["State"].unique())
State_data = df[df["State"] == State_name]
st.write(f"Deaths in {State_name}:")
st.write(State_data.loc[:, ["COVID-19 Deaths"]].sum())
st.subheader("Deaths by Age Group")
# st.sidebar.selectbox("Select the Age Group",df['Age Group'].unique())
Age_group = st.sidebar.selectbox("Select an Age Group", df["Age Group"].unique())
Age_data = State_data[df["Age Group"] == Age_group]
st.write(f"Deaths in the {Age_group}:")
st.write(Age_data.loc[:, ["COVID-19 Deaths"]].sum())
#in this we are taking the user input and then we are showing the total deaths in that month
st.subheader("Deaths in selected Month and in selected State")
Month_name=st.sidebar.selectbox("Select a Month",df["Month"].unique())
Month_data=State_data[df["Month"]==Month_name]
st.write(f"Deaths in {Month_name}:")
st.write(Month_data.loc[:,["COVID-19 Deaths"]].sum())

#plots
st.subheader("Plots") #this plot is for the total deaths of age group
fig=px.bar(df,x="Age Group",y="COVID-19 Deaths",color="Sex",title="Deaths by Age Group")
st.write(fig)
#this plot is for the total deaths of state
fig2=px.bar(df,x="State",y="COVID-19 Deaths",color="Sex",title="Deaths by State")
st.write(fig2)
#this plot is for the total deaths of months
fig3=px.bar(df,x="Month",y="COVID-19 Deaths",title="Deaths by Month")
st.write(fig3)






# st.subheader("Deaths by Month")


# st.sidebar.selectbox("Select the Month",df['Month'].unique())





# Age_group = st.sidebar.selectbox("Select an Age Group", df["Age Group"].unique())
# Age_data = df[df["Age Group"] == Age_group]
# st.write(f"Deaths in {Age_group}:")
# st.write(Age_data[ ["COVID-19 Deaths"]].sum())






# # Show line chart of cases over time
# st.line_chart(country_data.set_index("Date")[["Confirmed", "Deaths", "Recovered"]])