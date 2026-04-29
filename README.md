# 🛒 BigBasket Product Rating Prediction

## 📌 Project Overview

This project focuses on predicting whether a product on BigBasket will be **highly rated (≥ 4.0)** based on pricing and category-related features.

The goal is to help businesses understand **what drives product ratings** and support **data-driven decision making**.

---

## 🎯 Problem Statement

In e-commerce platforms like BigBasket, product ratings play a crucial role in customer purchase decisions.

However, businesses often struggle to understand:

* What factors influence high ratings?
* How pricing impacts customer satisfaction?
* Which product categories perform better?

👉 This project solves this by building a **machine learning classification model** to predict high-rated products.

---

## 📊 Dataset

* Source: Kaggle (BigBasket Product Dataset)
* Total Records: ~27,000+
* Features:

  * Product Name
  * Category & Sub-category
  * Brand
  * Market Price
  * Sale Price
  * Rating
  * Description

---

## 🧹 Data Preprocessing

* Handled missing values in `rating` using:

  * Category-wise mean
  * Global median fallback
* Removed rows with missing critical fields (product, brand, description)
* Removed duplicates

---

## ⚙️ Feature Engineering

* Created binary target variable:

  * `is_high_rated = 1 (rating ≥ 4.0)`
  * `is_high_rated = 0 (otherwise)`
* Encoded `sub_category` using Label Encoding

👉 Final features used for modeling:

* `market_price`
* `sale_price`
* `sub_cat_encoded`

---

## ⚖️ Handling Imbalanced Data

* Dataset was imbalanced
* Applied **SMOTE (Synthetic Minority Oversampling Technique)** on training data

---

## 🤖 Models Used

| Model               | Technique                     |
| ------------------- | ----------------------------- |
| Logistic Regression | Scaled + SMOTE                |
| KNN                 | Scaled + SMOTE                |
| SVM                 | Scaled + SMOTE                |
| Random Forest       | SMOTE                         |
| Gradient Boosting   | SMOTE                         |
| XGBoost             | SMOTE + Hyperparameter Tuning |

---

## 🔧 Hyperparameter Tuning

* **RandomizedSearchCV** → XGBoost, Random Forest
* **GridSearchCV** → Gradient Boosting

---

## 📈 Model Performance (F1 Score)

| Model               | F1 Score        |
| ------------------- | --------------- |
| Logistic Regression | 0.62            |
| KNN                 | 0.64            |
| SVM                 | 0.58            |
| Random Forest       | 0.66            |
| Gradient Boosting   | 0.68            |
| XGBoost             | 0.69            |
| ✅ Tuned XGBoost     | **0.70 (Best)** |

---

## 🏆 Final Model

👉 **Tuned XGBoost** selected based on highest F1-score

---

## 📊 Key Insights

* Products with **better pricing strategies** tend to have higher ratings
* Certain **sub-categories consistently perform better**
* Balanced pricing improves customer perception
* Extreme or unusual pricing patterns lead to lower predicted ratings

---

## 💼 Business Impact

This project can help e-commerce businesses:

### 📌 Pricing Strategy Optimization

* Identify optimal price ranges for better ratings
* Avoid overpricing or unrealistic discounts

### 📌 Product Performance Analysis

* Understand which categories drive high ratings
* Focus on high-performing segments

### 📌 Inventory Planning

* Stock products likely to perform well
* Reduce low-performing inventory

### 📌 Customer Satisfaction Improvement

* Improve product offerings based on rating patterns

---

## 🚀 Streamlit App

An interactive web app was built using Streamlit to predict product ratings in real-time.

### Features:

* User-friendly interface
* Real-time prediction
* Input validation (prevents unrealistic pricing)

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Imbalanced-learn (SMOTE)
* Streamlit

---

## 📂 Project Structure

```
├── app.py
├── xgb_model.pkl
├── columns.pkl
├── label_encoder_subcat.pkl
├── notebook.ipynb
└── README.md
```

---

## 🧠 Learning Outcomes

* Handling real-world messy data
* Feature engineering & preprocessing
* Working with imbalanced datasets
* Model selection & evaluation using F1-score
* Hyperparameter tuning
* Model deployment using Streamlit

---

## 🔮 Future Improvements

* Add more features (brand, category encoding, text features)
* Improve model accuracy
* Deploy app on cloud (Streamlit Cloud / AWS)
* Add dashboard visualizations

---

## 🙌 Conclusion

This project demonstrates how machine learning can be used to **predict product success** and support **business decision-making in e-commerce**.

---

## 👤 Author

Abhijeet Mishra
