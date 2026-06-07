import streamlit as st
import pandas as pd
import pickle
import pymysql
import base64
import os

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





#background image

def get_base64(image_file):
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_path = os.path.join(os.path.dirname(__file__), "Truck_bg.png")
img = get_base64(img_path)

st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}

    [data-testid="stSidebar"] {{
        background: rgba(0,0,0,0.85);
    }}
    </style>
    """,
    unsafe_allow_html=True
)


#Title

st.markdown("""
<h1 style="
font-size:52px;
font-weight:900;
color:#FFD700;
text-align:center;
text-shadow:
    0 0 10px #00BFFF,
    0 0 20px #00BFFF,
    0 0 30px #00BFFF;
">
 Delivery Time Prediction
</h1>

<p style="
font-size:20px;
text-align:center;
color:#C0C0C0;
text-shadow:0 0 10px rgba(0,0,0,0.8);
">
Estimate delivery duration with machine learning insights
</p>
""", unsafe_allow_html=True)

#MY SQL

conn=pymysql.connect(
    host="localhost",
    user="root",
    password="Athul5555@",
    database="delivery"
)

cursor=conn.cursor()

#Create Table

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prediction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    distance_km FLOAT,
    order_prep_time_min INT,
    traffic_index FLOAT,
    num_items INT,
    is_weekend INT,
    order_hour INT,
    weather_condition VARCHAR(50),
    vehicle_type VARCHAR(50),
    predicted_delivery_time FLOAT
    )
"""
)


conn.commit()

#load


BASE_DIR = os.path.dirname(__file__)  # this is pages/

model = pickle.load(open(os.path.join(BASE_DIR, "xg_boost.save"), "rb"))
weather_encoder = pickle.load(open(os.path.join(BASE_DIR, "weather_enc.save"), "rb"))
vehicle_encoder = pickle.load(open(os.path.join(BASE_DIR, "vehicle_enc.save"), "rb"))

# model=pickle.load(open('xg_boost.save', 'rb'))
# weather_encoder=pickle.load(open('weather_enc.save', 'rb'))
# vehicle_encoder=pickle.load(open('vehicle_enc.save', 'rb'))

st.set_page_config(page_title="Delivery Time Prediction")

st.write("")
st.write("")

#Inputs

distance_kms=st.number_input(
    "Distance(km)",
    min_value=0.0,
    value=5.0
)

order_prep_time_min=st.number_input(
    "Preperation Time (min)",
    min_value=0,
    value=15
)

traffic_index=st.slider("Traffic Index",
                        min_value=0.0,
                        max_value=10.0,
                        value=5.0
                        )

num_items=st.number_input(
    "Number of Items",
    min_value=1,
    value=2
)

is_weekend=st.selectbox(
    "Weekend?",
    [0,1]
)

order_hour=st.slider(
    "Order Hour",
    0,
    23,
    12
)

weather_condition=st.selectbox(
    "Weather Condition",
    weather_encoder.classes_
)

vehicle_type=st.selectbox(
    "Vehicle Type",
    vehicle_encoder.classes_
)


#Predict

if st.button("Predict Delivery Time"):

    try:

        weather_encoded=weather_encoder.transform([weather_condition])[0]
        vehicle_encoded=vehicle_encoder.transform([vehicle_type])[0]

        features=[[
            distance_kms,
            order_prep_time_min,
            traffic_index,
            num_items,
            is_weekend,
            order_hour,
            weather_encoded,
            vehicle_encoded
        ]]

        pred=model.predict(features)

        import time

        # Loading Animation
        progress_text = st.empty()
        progress_bar = st.progress(0)

        for i in range(100):
            progress_text.text(f"🚚 Calculating Delivery Time... {i + 1}%")
            time.sleep(0.01)
            progress_bar.progress(i + 1)

        progress_bar.empty()
        progress_text.empty()




        placeholder = st.empty()

        for i in range(int(pred[0]) + 1):
            placeholder.markdown(
                f"""
                <div style="
                    background: rgba(0,123,255,0.85);
                    padding:25px;
                    border-radius:20px;
                    text-align:center;
                    color:white;
                    margin-bottom:20px;
                ">
                    <h2>🚚 Estimated Delivery Time</h2>
                    <h1 style="color:#FFD700;">{i} Minutes</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(0.02)



        # Animated Prediction Card

        placeholder.markdown(
            f"""
            <div style="
                background: rgba(0, 80, 180, 0.75);
                backdrop-filter: blur(10px);
                padding:25px;
                border-radius:20px;
                text-align:center;
                color:white;
                box-shadow:0 8px 25px rgba(0,0,0,0.3);
            ">
                <div style="font-size:28px;">🚚 Estimated Delivery Time</div>
                <div style="font-size:48px;font-weight:bold;color:#FFD700;">
                    {pred[0]:.2f} Minutes
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )




        st.markdown(f"""
        <style>

        @keyframes glow {{
          0% {{ box-shadow: 0 0 10px rgba(0,123,255,0.5); }}
          50% {{ box-shadow: 0 0 30px rgba(0,123,255,0.9); }}
          100% {{ box-shadow: 0 0 10px rgba(0,123,255,0.5); }}
        }}

        .result-card {{
            animation: glow 2s infinite;
            background: rgba(0,123,255,0.85);
            padding:25px;
            border-radius:20px;
            text-align:center;
            color:white;
        }}

        </style>
        """, unsafe_allow_html=True)


        # Small Delay Before Metrics
        time.sleep(0.3)

        # Metrics
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "📦 Items",
                num_items
            )

        with col2:
            st.metric(
                "🛣 Distance",
                f"{distance_kms:.1f} km"
            )

        speed = distance_kms / (pred[0] / 60)
        with col3:
            st.metric("⚡ Avg Speed", f"{speed:.1f} km/h")

        #kpi css

        st.markdown("""
        <style>
        [data-testid="stMetric"]{
            background: rgba(0,0,0,0.45);
            backdrop-filter: blur(8px);
            padding: 15px;
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,0.2);
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
        <style>

        [data-testid="stMetric"]{
            transition: all 0.3s ease;
        }

        [data-testid="stMetric"]:hover{
            transform: translateY(-8px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.4);
        }

        </style>
        """, unsafe_allow_html=True)


       #Traffic index css

        if traffic_index < 3:
            st.markdown("""
            <div style="
                background:#28a745;
                color:white;
                padding:12px;
                border-radius:12px;
                font-weight:bold;
                text-align:center;">
                🟢 Low Traffic - Fast Delivery Expected
            </div>
            """, unsafe_allow_html=True)

        elif traffic_index < 7:
            st.markdown("""
            <div style="
                background:#ffc107;
                color:black;
                padding:12px;
                border-radius:12px;
                font-weight:bold;
                text-align:center;">
                🚦 Moderate Traffic
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div style="
                background:#dc3545;
                color:white;
                padding:12px;
                border-radius:12px;
                font-weight:bold;
                text-align:center;">
                🔴 Heavy Traffic - Delivery May Be Delayed
            </div>
            """, unsafe_allow_html=True)

        #save to mysql

        cursor.execute("""
        INSERT INTO predictions(
            distance_km,
            order_prep_time_min,
            traffic_index,
            num_items,
            is_weekend,
            order_hour,
            weather_condition,
            vehicle_type,
            predicted_delivery_time
            
        )VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        
        """,
        (
            distance_kms,
            order_prep_time_min,
            traffic_index,
            num_items,
            is_weekend,
            order_hour,
            weather_condition,
            vehicle_type,
            float(pred[0])
        ))

        conn.commit()

    except:
        st.error("⚠ Please enter valid values in all fields")


