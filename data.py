import streamlit as st
import pandas as pd
import joblib

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Car Price Predictor | Henil Bhavsar",
    page_icon="🚗",
    layout="wide",
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: #ffffff;
        }
        .main {
            background-color: #0e1117;
        }
        h1, h2, h3, h4, h5 {
            color: #00b4d8 !important;
        }
        .stButton>button {
            background: linear-gradient(90deg, #00b4d8, #0077b6);
            color: white;
            border: none;
            padding: 0.7rem 1.3rem;
            border-radius: 10px;
            font-size: 1.1rem;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #0077b6, #023e8a);
            transform: scale(1.03);
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 0 15px rgba(0, 180, 216, 0.15);
            backdrop-filter: blur(10px);
        }
        .gradient-text {
            background: linear-gradient(90deg, #00b4d8, #90e0ef);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .footer {
            color: #adb5bd;
            text-align: center;
            margin-top: 40px;
            font-size: 0.9rem;
        }
        a {
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------- LOAD MODEL --------------------
model = joblib.load("car_price_model.pkl")
model_columns = joblib.load("model_columns.pkl")

# -------------------- NAVIGATION --------------------
st.sidebar.title("🚗 Car Price App")
page = st.sidebar.radio("Navigate", ["🏠 Home", "💰 Price Predictor", "👤 About Developer"])

# -------------------- HOME PAGE --------------------
if page == "🏠 Home":
    st.markdown(
        """
        <div style="text-align:center; padding:30px 0;">
            <h1 class="gradient-text" style="font-size:48px; margin-bottom:10px;">Car Price Predictor</h1>
            <p style="font-size:20px; color:#adb5bd;">AI-driven insights to estimate your car's market value in seconds.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.image(
        "https://cdn.dribbble.com/users/1770290/screenshots/15444518/media/f6e2b20b63d96d1180f5fcdf52f9da55.gif",
        use_container_width=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature Highlights
    st.subheader("✨ Why Use This App?")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class='glass-card'>
            <h3>⚙️ Machine Learning Model</h3>
            <p style='color:#adb5bd;'>Built using regression algorithms trained on real-world car data for precise predictions.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='glass-card'>
            <h3>🚀 Fast & Intuitive</h3>
            <p style='color:#adb5bd;'>Get your car price estimate in seconds with an easy-to-use, responsive interface.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='glass-card'>
            <h3>📊 Real-Time Predictions</h3>
            <p style='color:#adb5bd;'>Leverages data pipelines and dynamic encoding for real-time model predictions.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align:center;">
            <a href="?page=💰+Price+Predictor">
                <button style="
                    background: linear-gradient(90deg, #00b4d8, #0077b6);
                    color:white;
                    border:none;
                    padding:15px 40px;
                    border-radius:50px;
                    font-size:1.2rem;
                    cursor:pointer;
                    transition: all 0.3s ease;">
                    🔮 Try Prediction Now
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="footer">
            <p>Developed by <b>Henil Bhavsar</b> | Data Science Enthusiast 🧠</p>
            <p>© 2025 All Rights Reserved</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------- PRICE PREDICTOR --------------------
elif page == "💰 Price Predictor":
    st.markdown("<h1 style='text-align:center;'>💸 Car Price Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#adb5bd;'>Enter your car details below to get an estimated market price.</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        year = st.number_input("🛠 Manufacture Year", min_value=1990, max_value=2025, value=2020)
        mileage = st.number_input("⛽ Mileage (in km/l)", min_value=5.0, max_value=40.0, value=18.0, step=0.5)
    with col2:
        engine = st.number_input("⚙️ Engine Capacity (in CC)", min_value=500, max_value=5000, value=1500, step=100)
        fuel_type = st.selectbox("🔋 Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])

    # Prepare input
    input_data = pd.DataFrame({
        "year": [year],
        "mileage": [mileage],
        "engine": [engine],
        "fuel_type": [fuel_type]
    })

    input_data = pd.get_dummies(input_data)
    input_data = input_data.reindex(columns=model_columns, fill_value=0)

    st.markdown("---")
    predict_btn = st.button("🚀 Predict Price", use_container_width=True)

    if predict_btn:
        predicted_price = model.predict(input_data)[0]
        st.success(f"💰 **Estimated Car Price:** ${predicted_price:,.2f}")
        st.balloons()

# -------------------- ABOUT DEVELOPER --------------------
elif page == "👤 About Developer":
    st.markdown("""
        <div style="text-align:center; padding:20px;">
            <h1 class="gradient-text" style="font-size:42px;">👨‍💻 About the Developer</h1>
            <p style="color:#adb5bd;">Know more about the creator behind this AI-powered web app</p>
        </div>
    """, unsafe_allow_html=True)

    # Banner Image

    st.markdown("<br>", unsafe_allow_html=True)

    # Info Layout
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
            width=200
        )

    with col2:
        st.markdown("""
        <div class='glass-card'>
            <h3>🧑‍💼 Name:</h3>
            <p>Henil Bhavsar</p>
            <h3>📧 Email:</h3>
            <p><a href="mailto:henilbhavsar164@gmail.com" style="color:#00b4d8;">henilbhavsar164@gmail.com</a></p>
            <h3>📱 Contact:</h3>
            <p>+91 9714033439</p>
        </div>
        """, unsafe_allow_html=True)

    # Social Links
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align:center;">
            <h3>🌐 Connect with Me</h3>
            <p>
                <a href="https://www.linkedin.com/in/henil-bhavsar-18b45b311/" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40px" style="margin-right:20px;">
                </a>
                <a href="https://github.com/Henilll" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" width="40px">
                </a>
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="footer">
            <p>💡 Passionate about Data Science, Machine Learning & Web App Development.</p>
            <p>Building intelligent products that make data accessible and useful.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
