import streamlit as st
import base64




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




#page config

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ",
    layout="wide"
)

#title

st.markdown("""
<h1 style="
    color:#FF0F8FF;
    text-align:center;
    font-weight:bold;
">
ℹ About Delivery Time Prediction System
</h1>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<h2 style='color:#FFD700;'>
 Project Overview
</h2>
""", unsafe_allow_html=True)

st.write("""
The Smart Delivery Time Prediction System uses Machine Learning
to estimate delivery times based on various factors such as:

- Distance
- Traffic Conditions
- Weather Conditions
- Vehicle Type
- Order Preparation Time
- Number of Items
- Weekend/Weekday
- Order Hour

The system helps logistics companies improve delivery planning
and customer satisfaction.
""")

st.markdown("---")


st.markdown("""
<h2 style='color:#FFD700;'>
Machine Learning Model
</h2>
""", unsafe_allow_html=True)


st.write("""
The prediction model was trained using historical delivery data.

### Input Features
- Distance (km)
- Order Preparation Time
- Traffic Index
- Number of Items
- Weekend Indicator
- Order Hour
- Weather Condition
- Vehicle Type

### Output
- Predicted Delivery Time (minutes)
""")

st.markdown("---")


st.markdown("""
<h2 style='color:#FFD700;'>
Technologies Used
</h2>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.write("""
    ### Frontend
    - Streamlit
    - HTML
    - CSS
    """)

with col2:
    st.write("""
    ### Backend
    - Python
    - Pandas
    - NumPy
    - Scikit-Learn
    - MySQL
    """)

st.markdown("---")


st.markdown("""
<h2 style='color:#FFD700;'>
Application Modules
</h2>
""", unsafe_allow_html=True)


st.write("""
### Prediction
Predict delivery time using machine learning.

### Analytics
Visualize delivery trends and performance metrics.

### History
View previously predicted deliveries stored in the database.

### ℹ About
Project information and technical details.
""")

st.markdown("---")



st.markdown("""
<h2 style='color:#FFD700;'>
Key Features
</h2>
""", unsafe_allow_html=True)


st.success("✔ Real-time Delivery Time Prediction")
st.success("✔ MySQL Database Integration")
st.success("✔ Interactive Analytics Dashboard")
st.success("✔ Historical Prediction Tracking")
st.success("✔ User-Friendly Interface")






