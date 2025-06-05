import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Superstore Sales Dashboard", layout="wide")
st.title("📊 Superstore Sales Analytics Dashboard")

# ---------- Guidelines ----------
with st.expander("🧾 How to Use This App", expanded=True):
    st.markdown("""
    **Instructions:**
    - 📁 Upload your dataset or use the default one.
    - 🧭 Apply filters for Region, Category.
    - 🔍 Search Products using multi-select dropdown or input box.
    - 📈 View trends, region-wise breakdowns, recommendations.
    - 📥 Download filtered data after previewing it.
    """)

# ---------- Upload or Load Default ----------
st.sidebar.header("📁 Upload CSV Dataset")
uploaded_file = st.sidebar.file_uploader("Upload your own dataset", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file, encoding="ISO-8859-1")
    st.sidebar.success("✅ File uploaded")
else:
    data = pd.read_csv("Superstore_Enhanced.csv", encoding="ISO-8859-1")
    st.sidebar.info("Using default dataset")

# ---------- Preprocessing ----------
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Month-Year'] = data['Order Date'].dt.to_period("M").astype(str)
all_products = sorted(data["Product Name"].unique())

# ---------- Sidebar Filters ----------
regions = st.sidebar.multiselect("🌍 Select Region(s):", sorted(data["Region"].unique()), default=list(data["Region"].unique()))
categories = st.sidebar.multiselect("📦 Select Category(s):", sorted(data["Category"].unique()), default=list(data["Category"].unique()))
selected_products = st.sidebar.multiselect("🛒 Choose Products (from dropdown):", all_products)
typed_search = st.sidebar.text_input("🔍 Or type product name(s) [comma-separated]:")

# ---------- Apply Filters ----------
filtered_data = data[(data["Region"].isin(regions)) & (data["Category"].isin(categories))]

# Combine dropdown and text input for product filtering
product_keywords = set([p.lower() for p in selected_products])
if typed_search.strip():
    typed_list = [p.strip().lower() for p in typed_search.split(",")]
    product_keywords.update(typed_list)

if product_keywords:
    filtered_data = filtered_data[filtered_data["Product Name"].str.lower().apply(
        lambda x: any(kw in x for kw in product_keywords)
    )]

if filtered_data.empty:
    st.warning("⚠️ No matching data. Try modifying filters or product search.")
    st.stop()

# ---------- Preview Filtered Data ----------
st.subheader("🔎 Filtered Data Preview (Top 10 rows)")
st.dataframe(filtered_data.head(10))

# ---------- Visualizations ----------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 Monthly Sales Trend")
    month_sales = filtered_data.groupby("Month-Year")["Sales"].sum().reset_index()
    fig1 = px.line(month_sales, x="Month-Year", y="Sales", title="Monthly Sales Trend")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🌍 Sales by Region")
    region_sales = filtered_data.groupby("Region")["Sales"].sum().reset_index()
    fig2 = px.bar(region_sales, x="Region", y="Sales", color="Region", title="Sales by Region")
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("📦 Category by Region")
    cat_region = filtered_data.groupby(["Region", "Category"])["Sales"].sum().reset_index()
    fig3 = px.bar(cat_region, x="Region", y="Sales", color="Category", barmode="group", title="Category-wise Sales by Region")
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("🧠 Recommendation")
    top_product = filtered_data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(1).index[0]
    top_cat = filtered_data["Category"].mode()[0]
    st.info(f"📌 Based on your filters, customers in **{', '.join(regions)}** often buy **{top_cat}** items like **{top_product}**.")

# ---------- Download ----------
st.download_button(
    label="⬇ Download Filtered Data as CSV",
    data=filtered_data.to_csv(index=False).encode('utf-8'),
    file_name="filtered_superstore_data.csv",
    mime="text/csv"
)

st.markdown("---")
st.caption("Built with ❤️ by Nithish | Streamlit-based Sales Dashboard")
