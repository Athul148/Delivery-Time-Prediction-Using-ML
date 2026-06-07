import streamlit as st
import base64
import pandas as pd
import pymysql


st.markdown("""
<h1 style="
    color:#FF0F8FF;
    text-align:left;
    font-weight:bold;
">
History
</h1>
""", unsafe_allow_html=True)


#css sidebar


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


# Database Connection

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Athul5555@",
        database="delivery"
    )

@st.cache_data(ttl=30)
def load_history():
    conn = get_connection()

    query = """
    SELECT *
    FROM predictions
    ORDER BY id DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

df = load_history()

st.dataframe(df, use_container_width=True)



#filter

st.sidebar.header("Filters")

vehicle = st.sidebar.multiselect(
    "Vehicle Type",
    options=df["vehicle_type"].unique(),
    default=df["vehicle_type"].unique()
)

weather = st.sidebar.multiselect(
    "Weather",
    options=df["weather_condition"].unique(),
    default=df["weather_condition"].unique()
)

filtered_df = df[
    (df["vehicle_type"].isin(vehicle)) &
    (df["weather_condition"].isin(weather))
]

st.dataframe(filtered_df, use_container_width=True)

#download

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name="delivery_history.csv",
    mime="text/csv"
)