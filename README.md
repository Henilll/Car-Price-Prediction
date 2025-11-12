# Car-Price-Prediction


# 🚗 Car Price Predictor

## 🧠 AI-Powered Web App to Estimate Car Resale Value

A sleek and interactive Machine Learning web application that predicts the estimated resale price of a car based on its specifications. Built with Python, Streamlit, and Scikit-learn, featuring a modern dark-themed UI and real-time model inference.

---
## Live Demo:https://car-price-prediction-henil.streamlit.app/

## 🏗️ Tech Stack

| Category | Technologies |
|-----------|---------------|
| **Frontend** | Streamlit, HTML, CSS (Custom Styling) |
| **Backend / ML** | Python, Pandas, Scikit-learn, Joblib |
| **Modeling** | Linear Regression (Custom trained) |
| **Deployment** | Streamlit Cloud / Localhost |
| **Version Control** | Git & GitHub |

---

## 🎯 Features

✅ User-Friendly Interface – Modern, responsive dark theme  
✅ Real-Time Predictions – Instant ML model inference  
✅ Multiple Input Parameters – Year, Mileage, Engine, Fuel Type  
✅ Interactive Visuals – Dynamic price display with animations  
✅ Developer Info Page – Includes contact and portfolio links  
✅ Fully Deployable – Ready for Streamlit Cloud or local use  

---

## 🧩 Project Structure

```
Car-Price-Predictor/
│
├── app.py                # Streamlit web app
├── car_price_model.pkl   # Trained ML model
├── model_columns.pkl     # Model input columns
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/Henilll/Car-Price-Predictor.git
cd Car-Price-Predictor
```

### 2️⃣ Create & activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # for Windows
source venv/bin/activate # for macOS/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app
```bash
streamlit run app.py
```

Then open your browser at 👉 http://localhost:8501

---

## 🧮 Model Details

- **Algorithm:** Linear Regression  
- **Target Variable:** Car Price  
- **Input Features:** Year, Mileage, Engine Size, Fuel Type  
- **Encoding:** One-Hot Encoding for categorical variables  
- **Persistence:** Model serialized using joblib

---

## 👨‍💻 Developer Info

**Name:** Henil Bhavsar  
**Email:** henilbhavsar164@gmail.com  
**Contact:** +91 9714033439  

### 🔗 Connect with Me
LinkedIn:https://www.linkedin.com/in/henil-bhavsar-18b45b311/  
GitHub: https://github.com/Henilll

---

## 🚀 Deployment

You can easily deploy this project on:

- Streamlit Cloud
- Render
- Railway.app
- HuggingFace Spaces

Example command for Streamlit Cloud:
```
streamlit run app.py
```

---

## 💬 Future Enhancements

🔹 Add visualizations for predicted price distribution  
🔹 Include more car attributes (brand, transmission, etc.)  
🔹 Integrate REST API for external model access  
🔹 Add database for user data storage  

---

## 🏁 Conclusion

This project demonstrates:
- Real-world Machine Learning deployment
- Clean, interactive UI/UX design
- End-to-end pipeline from model training → frontend integration

💡 Built with passion for Machine Learning and elegant design by Henil Bhavsar
