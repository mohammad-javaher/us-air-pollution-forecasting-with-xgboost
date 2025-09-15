# us-air-pollution-forecasting-with-xgboost

# 🌍 US Air Pollution Forecasting with XGBoost  

This project uses **XGBoost** to forecast daily levels of major air pollutants in the United States, including:  

- 🟢 **CO** (Carbon Monoxide)  
- 🟡 **NO₂** (Nitrogen Dioxide)  
- 🔵 **O₃** (Ozone)  
- 🔴 **SO₂** (Sulfur Dioxide)  

The model is trained on historical air pollution data (2000–2016) and predicts pollutant levels for future dates using **time-derived features**.  

---

## 🚀 Features
- Time series forecasting with **XGBoost**  
- Separate trained models for each pollutant  
- Interactive **Streamlit app** to test predictions  
- Forecast trend visualization  

---

## 📂 Project Structure
```
├── notebooks # Jupyter notebooks for training & EDA
├── models # Saved XGBoost models (JSON format)
├── streamlit_app.py # Streamlit demo app
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

## ⚙️ Installation

Clone the repository:
```bash
git clone https://github.com/mohammad-javaher/us-air-pollution-forecasting-with-xgboost.git
cd us-air-pollution-forecasting-with-xgboost
```
## Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
```

## 🖥️ Running the Streamlit App

To launch the interactive web app locally:
```
streamlit run streamlit_app.py
```
Then open the link (usually http://localhost:8501) in your browser.

## 🌐 Online Demo

Try the deployed app here:
👉 [Live Demo](https://us-air-pollution-forecasting-with-xgboost-3utoasxvrezfjdant28j.streamlit.app/)

## 🛠️ Technologies Used

Python 3.10+

XGBoost for forecasting

Pandas / NumPy for feature engineering

Matplotlib for visualization

Streamlit for interactive deployment

# 👤 Author

Mohammad Javaher
📧 mohammadjavaaher@gmail.com
🔗 [[LinkedIn]](https://www.linkedin.com/in/mohammad-javaher/)
  [[GitHub Profile]](https://github.com/mohammad-javaher/)
