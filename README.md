# ✈️ Flight Dashboard – Streamlit App

This is an interactive Streamlit dashboard for analyzing flight data.  
It provides visual insights with filters (airline, year, source, destination, etc.) across multiple pages.

---

## 🚀 Features
- 📊 Multi-page dashboard (Overview, Delays & Cancellations, Route Performance)
- 🔍 Filter by Airline, Year, Source, Destination
- 🗂️ Large dataset (flights_cleaned.csv ~ 700MB)
- ⚡ Data caching with `st.cache_data` for faster reloads
- ☁️ Hosted on Streamlit Cloud

---

## 🛠️ Tech Stack
- Python 3.x
- [Streamlit](https://streamlit.io/)
- Pandas & NumPy
- Plotly, Matplotlib, Seaborn
- Folium & streamlit-folium

---

## 📂 Dataset
- Original dataset stored in **Google Drive** (public link, auto-loaded in app).  
- No need to keep dataset in GitHub repo.

---

## 📌 Pages & Visualizations

### Overview
- Total Flights, Unique Airlines, Routes, and Airports
- Top 10 Airlines by Flight Count
- Top 10 Busiest Routes
- Monthly Flight Trends
- Top Airports by Traffic (Interactive Map)

### Delays & Cancellations
- Average Arrival Delay by Airline
- Monthly Cancellation Rate
- Cancellation Reasons Breakdown

### Route Performance
- Top 10 Congested Routes
- Heatmap of Average Arrival Delays (Top 20 Routes)

### Filters
- Multi-select Airline filter
- Multi-select Year filter
- Page navigation: Overview / Delays & Cancellations / Route Performance

---

## 📊 Visualizations

The dashboard includes **9 interactive visualizations**:
1. KPI Metrics (Total Flights, Airlines, Routes, Airports)  
2. Top 10 Airlines by Flight Count  
3. Top 10 Busiest Routes  
4. Monthly Flight Trend  
5. Top Airports by Traffic Map (Folium)  
6. Average Arrival Delay by Airline  
7. Monthly Cancellation Rate  
8. Cancellation Reasons Breakdown (Pie Chart)  
9. Route Delay Heatmap (Top 20 Routes)  

---

## Installation & Run Locally

1. Clone the repository:
```bash
git clone <your-repo-url>
cd airfly-dashboard
pip install -r requirements.txt
streamlit run app.py
