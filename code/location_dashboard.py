
#location_dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout="wide")


df = pd.read_csv('./cache/tickets_in_top_locations.csv')


st.title('Top Locations for Parking Tickets within Syracuse')
st.caption('This dashboard shows the parking tickets that were issued in the top locations with $1,000 or more in total aggregate violation amounts.')

locations = df['location'].unique()

location = st.selectbox('Select a location:', locations)
if location:
    filtered_df = df[df['location'] == location]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total tickets issued", filtered_df.shape[0])
        fig1, ax1 = plt.subplots()
        ax1.set_title('Tickets Issued by Hour of Day')
        sns.barplot(data=filtered_df, x="hourofday", y="count", estimator="sum", hue="hourofday", ax=ax1)
        st.pyplot(fig1)

    with col2:
        st.metric("Total amount", f"$ {filtered_df['amount'].sum()}")
        fig2, ax2 = plt.subplots()
        ax2.set_title('Tickets Issued by Day of Week')
        sns.barplot(data=filtered_df, x="dayofweek", y="count", estimator="sum", hue="dayofweek", ax=ax2)
        st.pyplot(fig2)

    st.map(filtered_df[['lat', 'lon']])

'''
# location_dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure the Streamlit page layout
st.set_page_config(layout="wide")

# Load the dataset
df = pd.read_csv('./cache/tickets_in_top_locations.csv')

# Dashboard title and description
st.title('Top Locations for Parking Tickets within Syracuse')
st.caption('This dashboard shows the parking tickets that were issued in the top locations with $1,000 or more in total aggregate violation amounts.')

# Dropdown for selecting a location
location = st.selectbox('Select a location:', df['location'].unique())

if location:
    # Filter data for the selected location
    filtered_df = df[df['location'] == location]

    # Display metrics and visualizations in two columns
    col1, col2 = st.columns(2)

    # Column 1: Total tickets and tickets by hour of day
    with col1:
        st.metric("Total tickets issued", filtered_df.shape[0])
        sns.set_theme(style="whitegrid")
        fig1, ax1 = plt.subplots()
        sns.barplot(data=filtered_df, x="hourofday", y="count", estimator="sum", ax=ax1)
        ax1.set_title('Tickets Issued by Hour of Day')
        st.pyplot(fig1)

    # Column 2: Total amount and tickets by day of week
    with col2:
        total_amount = filtered_df['amount'].sum()
        st.metric("Total amount", f"$ {total_amount:,.2f}")
        fig2, ax2 = plt.subplots()
        sns.barplot(data=filtered_df, x="dayofweek", y="count", estimator="sum", ax=ax2)
        ax2.set_title('Tickets Issued by Day of Week')
        st.pyplot(fig2)

    # Display a map of ticket locations
    st.map(filtered_df[['lat', 'lon']])
'''