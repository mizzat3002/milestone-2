# Stroke Prediction 

## Repository Outline

1. README.md - Penjelasan gambaran umum project
2. P1M2_muhammad_izzat.ipynb - Notebook utama berisi EDA, preprocessing, training, dan evaluasi model
3. P1M2_muhammad_izzat_inf.ipynb - Notebook inference untuk mencoba prediksi menggunakan model yang sudah disimpan
4. model_stroke.pkl - File model Random Forest terbaik hasil Hyperparameter Tuning
5. stroke_data.csv - Dataset rekam medis pasien yang digunakan untuk training

## Problem Background
Stroke adalah salah satu penyebab kematian terbesar di indonesia. deteksi dini sangat penting agar pasien yang berisiko bisa mendapat penanganan lebi cepet. project ini membangun model klasifikasi untuk memprediksi apakah seseorang berisiko terkena stroke 

## Project Output
Ouput berupa model klasifikasi random forest yang bisa memprediksi apakah seseorang berisiko stroke atau tidak, disimpan dalam file model_stroke.pkl.

## Data
Dataset rekam medis 5.110 pasien dari Kaggle. ada 12 kolom mulai dari usia, BMI, kadar gula darah, sampai status merokok. dari seluruh data, cuma sekitar 5% pasien yang positif stroke, jadi datanya tidak seimbang

## Method
supervised learning - binary classification menggunakan 5 algoritma:

semua  model dibangun pakai pipeline, dievaluasi pakai cross validation dengan metric f1 score, lalu dituning pakai gridsearch. Random Forest keluar sebagai model terbaik dengan recall 74% setelah tuning.

## Stacks
Bahasa : python

Library ; Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Joblib

## Reference
https://huggingface.co/spaces/mizzat3002/Stroke-Prediction

https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

https://www.who.int/data/gho/data/themes/topics/topic-details/GHO/body-mass-index

https://www.childrenshospital.org/conditions-treatments/neonatal-stroke

---
