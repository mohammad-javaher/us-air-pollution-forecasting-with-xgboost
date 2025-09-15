import streamlit as st
import pandas as pd
import xgboost as xgb

# Load trained models
regO3 = xgb.XGBRegressor()
regO3.load_model("O3_model.json")

regCO = xgb.XGBRegressor()
regCO.load_model("CO_model.json")

regNO2 = xgb.XGBRegressor()
regNO2.load_model("NO2_model.json")

regSO2 = xgb.XGBRegressor()
regSO2.load_model("SO2_model.json")

# Features used during training
FEATURES = ['dayofyear', 'quarter', 'month', 'year', 'weekofyear']

def create_features(df):
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    df['weekofyear'] = df.index.isocalendar().week
    return df

st.title("🌍 Air Pollution Forecasting with XGBoost")

# --- Date Range Selector ---
date_range = st.date_input(
    "Select a date range for prediction",
    value=(pd.Timestamp("2025-01-01"), pd.Timestamp("2025-02-01"))
)

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
    st.write(f"📅 Forecasting from {start_date} to {end_date}")

    # Create future dataframe
    future_range = pd.date_range(start_date, end_date, freq="D")
    future_df = pd.DataFrame(index=future_range)
    future_df = create_features(future_df)

    # Predict with all models
    future_df['O3_pred'] = regO3.predict(future_df[FEATURES])
    future_df['CO_pred'] = regCO.predict(future_df[FEATURES])
    future_df['NO2_pred'] = regNO2.predict(future_df[FEATURES])
    future_df['SO2_pred'] = regSO2.predict(future_df[FEATURES])

    # --- Separate Plots ---
    st.subheader("O3 Forecast")
    st.line_chart(future_df[['O3_pred']])

    st.subheader("CO Forecast")
    st.line_chart(future_df[['CO_pred']])

    st.subheader("NO2 Forecast")
    st.line_chart(future_df[['NO2_pred']])

    st.subheader("SO2 Forecast")
    st.line_chart(future_df[['SO2_pred']])

    # Show table
    st.subheader("Predicted Values Table")
    st.dataframe(future_df[['O3_pred', 'CO_pred', 'NO2_pred', 'SO2_pred']].round(3))
