import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import st_folium

# --------------------------
# Page Config
# --------------------------
st.set_page_config(page_title="AirFly Insights Dashboard", layout="wide")

# --------------------------
# Load Data
@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?id=1WQcFOct-jLjxDgzig3joliyENoXRxEND"
    df = pd.read_csv(url)
    df["FL_DATE"] = pd.to_datetime(df["FL_DATE"], errors='coerce')
    df["Year"] = df["FL_DATE"].dt.year
    df["Month"] = df["FL_DATE"].dt.month
    df["WeekdayName"] = df["FL_DATE"].dt.day_name()
    df["Route"] = df["ORIGIN"] + " → " + df["DEST"]
    df["CityPair"] = df["ORIGIN_CITY"] + " → " + df["DEST_CITY"]
    return df

df = load_data()

# --------------------------
# Sidebar
# --------------------------
st.sidebar.title("AirFly Dashboard")

# Global filters
airlines = st.sidebar.multiselect("Airline", sorted(df['AIRLINE'].unique()))
years = st.sidebar.multiselect("Year", sorted(df['Year'].unique()))

# Apply filters
df_filtered = df.copy()
if airlines:
    df_filtered = df_filtered[df_filtered['AIRLINE'].isin(airlines)]
if years:
    df_filtered = df_filtered[df_filtered['Year'].isin(years)]

page = st.sidebar.radio("Go To:", ["Overview", "Delays & Cancellations", "Route Performance"])

# --------------------------
# PAGE 1: Overview
# --------------------------
if page == "Overview":
    st.title("✈️ Airline Operations Overview")

    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Flights", f"{df_filtered['FL_NUMBER'].count():,}")
    col2.metric("Unique Airlines", df_filtered['AIRLINE'].nunique())
    col3.metric("Unique Routes", df_filtered['Route'].nunique())
    col4.metric("Unique Airports", df_filtered['ORIGIN'].nunique())

    st.markdown("---")

    # Top Airlines
    top_airlines = df_filtered['AIRLINE'].value_counts().head(10).reset_index()
    top_airlines.columns = ['AIRLINE','count']
    fig1 = px.bar(top_airlines, x='count', y='AIRLINE', orientation='h',
                  title="Top 10 Airlines by Flight Count", color='count', color_continuous_scale="Blues")
    st.plotly_chart(fig1, use_container_width=True)

    # Top Routes
    top_routes = df_filtered['Route'].value_counts().head(10).reset_index()
    top_routes.columns = ['Route','count']
    fig2 = px.bar(top_routes, x='count', y='Route', orientation='h',
                  title="Top 10 Busiest Routes", color='count', color_continuous_scale="Oranges")
    st.plotly_chart(fig2, use_container_width=True)

    # Monthly Flight Trend
    monthly = df_filtered.groupby('Month')['FL_NUMBER'].count()
    fig3 = px.line(x=monthly.index, y=monthly.values, markers=True,
                   title="Monthly Flight Trend")
    fig3.update_layout(xaxis_title="Month", yaxis_title="Flights")
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("---")

    # Folium Map
    st.subheader("Top Airports by Traffic (Map)")
    airport_locations = {
        'ATL': (33.6407, -84.4277), 'DFW': (32.8998, -97.0403), 'ORD': (41.9742, -87.9073),
        'DEN': (39.8561, -104.6737), 'CLT': (35.2139, -80.9431), 'LAX': (33.9416, -118.4085),
        'PHX': (33.4342, -112.0119), 'LAS': (36.0840, -115.1537), 'SEA': (47.4480, -122.3088),
        'MCO': (28.4294, -81.3089), 'SFO': (37.6213, -122.3790), 'JFK': (40.6413, -73.7781)
    }
    busiest_airports = df_filtered['ORIGIN'].value_counts().head(10).index
    avg_delays = df_filtered.groupby('ORIGIN')['ARR_DELAY'].mean()

    m = folium.Map(location=[39.8, -98.5], zoom_start=4)
    for airport in busiest_airports:
        if airport in airport_locations:
            lat, lon = airport_locations[airport]
            delay = avg_delays.get(airport, 0)
            folium.CircleMarker(
                location=[lat, lon],
                radius=6,
                popup=f"{airport}: {delay:.1f} min avg delay",
                color="blue",
                fill=True
            ).add_to(m)
    st_folium(m, width=700, height=500)

# --------------------------
# PAGE 2: Delays & Cancellations
# --------------------------
elif page == "Delays & Cancellations":
    st.title("⏱️ Delay & Cancellation Insights")

    # Avg Delay by Airline
    avg_delay = df_filtered.groupby("AIRLINE")['ARR_DELAY'].mean().reset_index()
    fig4 = px.bar(avg_delay, x='AIRLINE', y='ARR_DELAY',
                  title="Average Arrival Delay by Airline", color='ARR_DELAY', color_continuous_scale="Reds")
    st.plotly_chart(fig4, use_container_width=True)

    st.markdown("---")

    # Monthly Cancellation Rate
    monthly_cancel = df_filtered.groupby("Month")['CANCELLED'].mean() * 100
    fig5, ax = plt.subplots(figsize=(8,4))
    ax.plot(monthly_cancel.index, monthly_cancel.values, marker='o', color='red')
    ax.set_title("Monthly Cancellation Rate (%)")
    ax.set_xlabel("Month")
    ax.set_ylabel("Cancellation Rate %")
    st.pyplot(fig5)

    # Cancellation Reasons
    cancelled = df_filtered[df_filtered['CANCELLED'] == 1].copy()
    reason_map = {'A': 'Carrier', 'B': 'Weather', 'C': 'NAS', 'D': 'Security'}
    cancelled['Reason'] = cancelled['CANCELLATION_CODE'].map(reason_map)
    pie_counts = cancelled['Reason'].value_counts()
    fig6, ax = plt.subplots()
    ax.pie(pie_counts, labels=pie_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Cancellation Reasons Breakdown")
    st.pyplot(fig6)

# --------------------------
# PAGE 3: Route Performance
# --------------------------
elif page == "Route Performance":
    st.title("🛫 Route & Airport Performance")

    # Congested Routes
    top_routes = df_filtered['Route'].value_counts().head(10).reset_index()
    top_routes.columns = ['Route','count']
    fig7 = px.bar(top_routes, x='count', y='Route', orientation='h',
                  title="Top 10 Congested Routes", color='count', color_continuous_scale="Viridis")
    st.plotly_chart(fig7, use_container_width=True)

    st.markdown("---")

    # Heatmap of Delays
    st.subheader("Route Delay Heatmap (Top 20 Routes)")
    top_20 = df_filtered['Route'].value_counts().head(20).index
    df_top = df_filtered[df_filtered['Route'].isin(top_20)]
    delay_matrix = df_top.pivot_table(index='ORIGIN', columns='DEST', values='ARR_DELAY', aggfunc='mean')

    fig8, ax = plt.subplots(figsize=(10,6))
    sns.heatmap(delay_matrix, cmap='YlOrRd', annot=True, fmt=".1f", linewidths=.5, ax=ax)
    ax.set_title("Average Arrival Delay Heatmap (Top 20 Routes)")
    st.pyplot(fig8)






