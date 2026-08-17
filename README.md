# StrokeRisk: Sistem Deteksi Dini Stroke Menggunakan Machine Learning

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

## 📌 Project Overview
Stroke adalah salah satu penyebab utama kematian di Indonesia. Proyek ini bertujuan untuk membangun **sistem klasifikasi berbasis Machine Learning** yang dapat memprediksi risiko stroke seseorang berdasarkan metrik kesehatan, guna membantu deteksi dini dan tindakan pencegahan medis.

## ❓ Problem Statement
Deteksi dini sangat krusial dalam penanganan stroke. Tantangan utama dalam proyek ini adalah menangani **data yang tidak seimbang** (*imbalanced data*), di mana hanya sekitar 5% pasien dalam dataset yang terdiagnosis stroke, untuk membangun model prediksi yang handal dan sensitif terhadap kasus positif.

## 📊 Data & Metodologi
*   **Dataset:** Rekam medis 5.110 pasien (sumber: Kaggle), mencakup 12 fitur seperti usia, BMI, kadar gula darah, dan status merokok.
*   **Pendekatan:** Supervised Learning - Binary Classification.
*   **Alur Kerja:** Mengevaluasi 5 algoritma berbeda menggunakan *Pipeline* dan *Cross-Validation*. **Random Forest** terpilih sebagai model terbaik setelah melalui proses *Hyperparameter Tuning*.
*   **Performa:** Berhasil mencapai nilai **Recall 74%** setelah tuning, yang berarti model cukup sensitif dalam mendeteksi potensi stroke pada pasien.

## 🛠 Tech Stack
*   **Bahasa:** Python
*   **Library:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Joblib
*   **Deployment:** Streamlit (Hosted on Hugging Face Spaces)

## 📂 Struktur Repositori
1. `P1M2_muhammad_izzat.ipynb`: Notebook utama (EDA, Preprocessing, Training, Evaluasi).
2. `P1M2_muhammad_izzat_inf.ipynb`: Notebook inference untuk prediksi data baru.
3. `model_stroke.pkl`: File model Random Forest terbaik yang sudah di-tuning.
4. `stroke_data.csv`: Dataset rekam medis pasien.

## 🚀 Fitur Utama
*   **Model Klasifikasi Teroptimasi:** Menggunakan Random Forest yang telah dituning khusus untuk menangani data medis yang tidak seimbang.
*   **Aplikasi Web Interaktif:** User-friendly interface untuk melakukan prediksi risiko stroke secara real-time.
*   **Pipeline Terintegrasi:** Proses pembersihan data hingga prediksi dilakukan secara otomatis dalam satu alur kerja yang kokoh.

## 🔗 Link Proyek
*   **Demo Aplikasi:** [Stroke Prediction App di Hugging Face](https://huggingface.co/spaces/mizzat3002/Stroke-Prediction)
*   **Dataset Sumber:** [Kaggle Stroke Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)

---
**Developed by:** Muhammad Izzat (HCK-041)
