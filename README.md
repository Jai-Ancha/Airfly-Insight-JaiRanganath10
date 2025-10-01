# ✈️ AirFly Insights Dashboard

**AirFly Insights Dashboard** is an interactive Streamlit app for analyzing airline operations, delays, cancellations, and route performance using real flight data. The dashboard provides actionable insights via interactive visualizations and maps.

---

## 🚀 Features

- **Overview**
  - Total Flights, Unique Airlines, Routes, and Airports
  - Top 10 Airlines by Flight Count
  - Top 10 Busiest Routes
  - Monthly Flight Trends
  - Top Airports by Traffic (Interactive Map)

- **Delays & Cancellations**
  - Average Arrival Delay by Airline
  - Monthly Cancellation Rate
  - Cancellation Reasons Breakdown

- **Route Performance**
  - Top 10 Congested Routes
  - Heatmap of Average Arrival Delays (Top 20 Routes)

- **Filters**
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

##  Tech Stack

- Python 3.x  
- [Streamlit](https://streamlit.io/)  
- Pandas & NumPy  
- Plotly, Matplotlib, Seaborn  
- Folium & streamlit-folium  

---

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd airfly-dashboard


## Run the App
pip install streamlit plotly pandas numpy matplotlib seaborn folium streamlit-folium
streamlit run app.py
