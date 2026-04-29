import streamlit as st
import joblib
import pandas as pd
import numpy as np

# -------------------- LOAD FILES --------------------
model = joblib.load('xgb_model.pkl')
columns = joblib.load('columns.pkl')
le_sub = joblib.load('label_encoder_subcat.pkl')

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="BigBasket Predictor", page_icon="🛒", layout="centered")

# -------------------- HEADER --------------------
st.markdown("<h1 style='text-align: center;'>🛒 BigBasket Rating Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict whether a product will be HIGH rated ⭐</p>", unsafe_allow_html=True)

st.divider()

# -------------------- INPUT --------------------
st.subheader("📥 Enter Product Details")

col1, col2 = st.columns(2)

with col1:
    market_price = st.number_input("💰 Market Price", min_value=0.0, step=1.0)

with col2:
    sale_price = st.number_input("🏷️ Sale Price", min_value=0.0, step=1.0)

# Category selection
sub_categories = list(le_sub.classes_)
sub_category = st.selectbox("📦 Select Sub Category", sub_categories)

st.divider()

# -------------------- FEATURE ENGINEERING (same as training) --------------------
def prepare_input(market_price, sale_price, sub_category):
    sub_encoded = le_sub.transform([sub_category])[0]

    input_data = {
        'market_price': market_price,
        'sale_price': sale_price,
        'sub_cat_encoded': sub_encoded
    }

    df = pd.DataFrame([input_data])

    # Ensure all columns exist
    for col in columns:
        if col not in df.columns:
            df[col] = 0

    # Correct column order
    df = df[columns]

    return df

# -------------------- PREDICTION --------------------
if st.button("🔍 Predict Rating"):
    try:
        # 🚨 Validation
        if sale_price > market_price:
            st.warning("⚠️ Sale price should not be greater than market price")
        else:
            # Prepare input
            input_df = prepare_input(market_price, sale_price, sub_category)

            # Prediction
            prediction = model.predict(input_df)[0]
            prob = model.predict_proba(input_df)[0][1]

            st.subheader("📊 Prediction Result")

            if prediction == 1:
                st.success(f"✅ HIGH Rated Product ⭐ (Confidence: {prob:.2f})")
            else:
                st.error(f"❌ Not Highly Rated (Confidence: {prob:.2f})")

    except Exception as e:
        st.error(f"Error: {e}")