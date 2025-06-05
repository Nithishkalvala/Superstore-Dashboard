# 📊 Superstore Sales Analytics Dashboard

An interactive Streamlit web app for visualizing and analyzing Superstore sales data. Users can filter by region, category, or product and gain AI-powered insights — all in a user-friendly dashboard.

---

## 🚀 Features

- 📁 Upload your own dataset (or use the default one)
- 🔎 Search for multiple products at once
- 🗂️ Filter data by Region, Category, and Product
- 📈 Visualizations:
  - Monthly Sales Trends
  - Sales by Region
  - Category by Region
  - Dynamic KPI cards
- 💡 AI-generated recommendations based on filters
- 📤 Export filtered data or charts as CSV, PNG, or PDF
- 🔒 Optional user login and admin login (can be toggled off)

---

## 🗂️ Dataset

Default dataset used: `Superstore_Enhanced.csv`  
Format: CSV  
Contains: Order Date, Sales, Category, Sub-Category, Region, Product Name, etc.

---

## 🛠️ Technologies Used

- **Frontend & UI**: [Streamlit](https://streamlit.io/)
- **Data Processing**: [Pandas](https://pandas.pydata.org/)
- **Visualization**: [Plotly Express](https://plotly.com/python/plotly-express/)
- **Database (Optional)**: SQLite (for user management)

---
2.Install Requirements

pip install -r requirements.txt

3. Run the App
streamlit run app.py

4.☁️ Deploy to Streamlit Cloud
Push this folder to a GitHub repository.

Visit https://streamlit.io/cloud.

Click “New app”, select your repo and app.py.

Click “Deploy” — you're live!

📌 Notes
First-time users are shown a quick guide on top.

Users can use your dataset or upload their own.

Login and sign-up logic can be toggled or fully removed based on your use case.

You can extend this app with advanced features like email OTP verification, detailed product insights, or predictive analytics.


