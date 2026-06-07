import streamlit as st
import base64

st.set_page_config(
    page_title="Delivery Time Prediction",
    page_icon="🚚",
    layout="wide"
)


#css sidebar



#flicker


st.markdown("""
<style>

/* Remove animation */
[data-testid="stSidebarNav"] a{
    transition: none !important;
}

/* Prevent focus flash */
[data-testid="stSidebarNav"] a:focus,
[data-testid="stSidebarNav"] a:active{
    outline: none !important;
    box-shadow: none !important;
}

/* Hide navigation until styled */
[data-testid="stSidebarNav"]{
    visibility: visible;
}

</style>
""", unsafe_allow_html=True)



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


# BACKGROUND


def get_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()


img = get_base64("pages/Truck_bg.png")



#sidebar

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



#HERO SECTION

st.markdown("""
<div style="
text-align:center;
padding:40px;
">

<h1 style="
font-family:'Exo 2', sans-serif;
font-size:72px;
font-weight:900;
color:#F0F8FF;
margin-bottom:10px;
letter-spacing:3px;
text-transform:uppercase;">
Delivery Time Predictor
</h1>



<p style="
font-size:22px;
color:#CD7F32;">
AI-powered system to predict accurate delivery time in seconds
</p>

</div>
""", unsafe_allow_html=True)



#CARDS


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:CD7F32;">

    <h3>Fast Prediction</h3>
    <p>Get delivery time instantly using ML model</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;">

    <h3>Smart Analytics</h3>
    <p>Analyze delivery patterns & traffic impact</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px);
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;">

    <h3>History Tracking</h3>
    <p>Store and review past predictions</p>
    </div>
    """, unsafe_allow_html=True)

# CARD CSS

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div style="
    background: rgba(0,123,255,0.8);
    padding:25px;
    border-radius:20px;
    text-align:center;
    color:white;
    font-size:20px;
    font-weight:bold;
    box-shadow:0 10px 30px rgba(0,0,0,0.4);">

    Use the sidebar menu to start prediction

    </div>
    """, unsafe_allow_html=True)