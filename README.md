✈️ AirFly Insights Dashboard – Streamlit App

Live App: https://airfly-insight-lailanganath10-f5wwc7kqywqfva54zuywdf.streamlit.app/

An interactive Streamlit dashboard for exploring flight data and airline operations. The app provides dynamic visual insights with filters for Airline and Year across multiple pages.

🚀 Features

Multi-page dashboard:

Overview – Key KPIs, top airlines/routes, monthly trends, traffic map

Delays & Cancellations – Average arrival delays, cancellation rates, reasons breakdown

Route Performance – Top congested routes, route delay heatmap

Filters:

Multi-select Airline

Multi-select Year

Optimized data handling:

Uses Parquet format for faster loading and memory efficiency

Cached data with st.cache_data for improved performance

Hosted on Streamlit Cloud for easy access

📊 Visualizations

The dashboard includes 9 dynamic visualizations:

KPI Metrics – Total Flights, Airlines, Routes, Airports

Top 10 Airlines by Flight Count (Bar Chart)

Top 10 Busiest Routes (Bar Chart)

Monthly Flight Trend (Line Chart)

Top Airports by Traffic (Interactive Folium Map)

Average Arrival Delay by Airline (Bar Chart)

Monthly Cancellation Rate (Line Chart)

Cancellation Reasons Breakdown (Pie Chart)

Route Delay Heatmap (Top 20 Routes, Heatmap)

🛠 Tech Stack

Python 3.13+

Streamlit – Web app framework

Pandas & NumPy – Data processing

Plotly, Matplotlib, Seaborn – Visualizations

Folium & streamlit-folium – Interactive maps

Kaggle API – Dataset download

📂 Dataset

File: flights_cleaned_sample_25pct.parquet (~750,000 rows, 25% of full dataset)

Full dataset has 3 million rows; sample used for Streamlit Cloud memory limits.

Dataset is auto-downloaded via Kaggle API, so no need to store locally or in GitHub.

Kaggle Dataset: anchajairanganath/flights-cleaned

📌 Pages & Visualizations
Overview

Total Flights, Unique Airlines, Routes, Airports

Top 10 Airlines by Flight Count

Top 10 Busiest Routes

Monthly Flight Trends

Top Airports by Traffic (Interactive Map)

Delays & Cancellations

Average Arrival Delay by Airline

Monthly Cancellation Rate

Cancellation Reasons Breakdown (Pie Chart)

Route Performance

Top 10 Congested Routes

Heatmap of Average Arrival Delays (Top 20 Routes)

⚡ Installation & Run Locally

Clone the repository:

git clone <your-repo-url>
cd airfly-dashboard


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

📄 Files in Repository

app.py – Main Streamlit dashboard code

requirements.txt – All Python dependencies

.gitignore – Ignores dataset & temporary files

🌟 Notes

The app dynamically fetches data from Kaggle if not present locally.

Using the 25% sample Parquet file balances memory usage and dashboard accuracy.

Hosted live on Streamlit Cloud, so anyone can view or share the link directly.

💡 Improvements / Future Work

Allow users to select custom sample percentages for larger datasets.

Add interactive filters for routes and airports.

Expand dataset with real-time flight updates.
