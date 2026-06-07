import streamlit as st
import base64
import pymysql
import pandas as pd
import numpy as np
import plotly.express as px




st.markdown("""
<style>

/* Sidebar width */
[data-testid="stSidebar"]{
    width: 280px;
}

/* Navigation links */
[data-testid="stSidebarNav"] a{
    background: rgba(255,255,255,0.08);
    border-radius: 12px;
    margin: 8px 10px;
    padding: 12px !important;
    transition: all 0.3s ease;
    color: white !important;
    font-weight: 600;
}

/* Hover effect */
[data-testid="stSidebarNav"] a:hover{
    background: linear-gradient(
        90deg,
        #00BFFF,
        #007BFF
    );
    transform: translateX(8px);
    box-shadow: 0 0 15px rgba(0,191,255,0.8);
}

/* Active page */
[data-testid="stSidebarNav"] a[aria-current="page"]{
    background: linear-gradient(
        90deg,
        #00BFFF,
        #007BFF
    );
    color: white !important;
    font-weight: bold;
    box-shadow: 0 0 20px rgba(0,191,255,0.9);
}

/* Hide default Pages title */
[data-testid="stSidebarNav"] > div:first-child{
    display:none;
}

</style>
""", unsafe_allow_html=True)


#sidebar

def get_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("pages/Truck_bg.png")

st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

[data-testid="stSidebar"] {{
    background: rgba(0,0,0,0.85);
}}

[data-testid="stSidebar"] * {{
    color:white;
}}
</style>
""", unsafe_allow_html=True)


# PAGE CONFIG

st.set_page_config(page_title="Analytics Dashboard", layout="wide")


# TITLE SECTION

st.markdown(
    """
    <h1 style='text-align: center; color: color:#FF0000;'>
    Delivery Analytics Dashboard
    </h1>
    <p style='text-align: center; color: gray;'>
    Insights from delivery performance data
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

#database

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Athul5555@",
        database="delivery"
    )

@st.cache_data(ttl=10)
def load_data():
    conn = get_connection()

    query = """
    SELECT
        distance_km,
        order_prep_time_min,
        traffic_index,
        num_items,
        is_weekend,
        order_hour,
        weather_condition,
        vehicle_type,
        predicted_delivery_time
    FROM predictions
    """

    df = pd.read_sql(query, conn)
    conn.close()

    return df

df = load_data()


# SIDEBAR FILTERS


st.sidebar.header("🔍 Filters")

weather_filter = st.sidebar.multiselect(
    "Weather",
    options=df["weather_condition"].unique(),
    default=df["weather_condition"].unique()
)

vehicle_filter = st.sidebar.multiselect(
    "🚗 Vehicle Type",
    options=df["vehicle_type"].unique(),
    default=df["vehicle_type"].unique()
)

df = df[
    (df["weather_condition"].isin(weather_filter)) &
    (df["vehicle_type"].isin(vehicle_filter))
]


# KPI CARDS

col1, col2, col3, col4 = st.columns(4)


col1.metric("Total Orders", len(df))
col2.metric("Avg Distance", f"{df['distance_km'].mean():.2f} km")
col3.metric("Avg Delivery Time",
            f"{df['predicted_delivery_time'].mean():.2f} min")
col4.metric("Avg Items",
            f"{df['num_items'].mean():.1f}")

st.divider()


# ROW 1 - CHARTS

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        "<h3 style='color:#FFD700;'>Delivery Time Distribution</h3>",
        unsafe_allow_html=True
    )

    fig = px.histogram(
        df,
        x="predicted_delivery_time",
        nbins=20,
        title="Predicted Delivery Time Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    st.markdown(
        "<h3 style='color:#FFD700;'>Traffic Impact on Delivery Time</h3>",
        unsafe_allow_html=True
    )
    fig2 = px.box(
        df,
        x="traffic_index",
        y="predicted_delivery_time",
        title="Traffic Impact on Delivery Time"
    )

    st.plotly_chart(fig2, use_container_width=True)


# ROW 2 - RELATIONSHIP ANALYSIS

st.markdown(
    "<h3 style='color:#FFD700;'>Distance vs Delivery Time Relationship</h3>",
    unsafe_allow_html=True
)

fig3 = px.scatter(
    df,
    x="distance_km",
    y="predicted_delivery_time",
    color="weather_condition",
    size="num_items",
    hover_data=["vehicle_type"]
)

st.plotly_chart(fig3, use_container_width=True)

