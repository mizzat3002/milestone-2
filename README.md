# StrokeRisk: Early Detection System using Machine Learning

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

## 📌 Project Overview
Stroke remains one of the leading causes of death globally and in Indonesia. This project develops a **machine learning-based classification system** to predict an individual's stroke risk based on health metrics, enabling early intervention and preventative care.

## ❓ Problem Statement
Early detection is vital for stroke management. This project addresses the challenge of identifying high-risk individuals using medical data, specifically handling significant **data imbalance** (~5% positive cases) to create a reliable predictive model.

## 📊 Data & Methods
*   **Dataset:** 5,110 patient records from Kaggle, covering 12 features including age, BMI, glucose levels, and smoking status.
*   **Approach:** Supervised Binary Classification.
*   **Model Pipeline:** Evaluated 5 different algorithms using Pipelines and Cross-Validation. **Random Forest** was selected as the champion model after Hyperparameter Tuning, achieving a **Recall of 74%**.

## 🛠 Tech Stack
*   **Languages:** Python
*   **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Joblib
*   **Deployment:** Streamlit (Hosted on Hugging Face)

## 🚀 Key Features
*   **Random Forest Classifier:** Optimized for handling imbalanced medical data.
*   **Interactive Web App:** User-friendly interface for real-time stroke risk prediction.
*   **Pipeline Integrated:** Robust end-to-end processing (preprocessing -> model -> prediction).

## 🔗 Project Links
*   **Interactive Demo:** [Stroke Prediction App](https://huggingface.co/spaces/mizzat3002/Stroke-Prediction)
*   **Dataset:** [Kaggle Stroke Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

---
**Developed by:** Muhammad Izzat (HCK-041)
