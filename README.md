# 🤖 Employee Performance Predictor using AI & Data Analytics

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data--Analysis-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview

This project builds an **end-to-end Employee Performance Prediction System** using Machine Learning and AI.

It helps organizations:

* 📊 Predict employee performance (High / Medium / Low)
* 🧠 Identify key performance drivers
* 📉 Detect low-performing employees early
* 📈 Support HR decisions (promotion, training, retention)
* ⚡ Provide a real-time interactive dashboard

---

## 🎥 Demo Video

[![Watch Video](images/Video Project 2.mp4)](images/Video Project 2.mp4)

---

## 📊 Dashboard Preview

*(Add dashboard screenshots here later if needed)*

---

## 🛠 Problem Statement

Companies face major HR challenges:

* ❌ Subjective performance evaluations
* ❌ Late identification of low performers
* ❌ Poor training decisions
* ❌ High employee attrition

---

## ✅ Solution

This system provides:

* AI-based performance prediction
* Data-driven HR insights
* Feature importance analysis
* Interactive dashboard for decision-making

---

## 🏭 Industry Relevance

| Industry     | Application                      |
| ------------ | -------------------------------- |
| IT Companies | Employee performance tracking    |
| HR Analytics | Data-driven decisions            |
| Consulting   | Workforce optimization           |
| Enterprises  | Promotion & retention strategies |

---

## 📊 Business Impact

* 📉 Early detection of low performers
* 💰 Reduced HR decision cost
* 📈 Improved employee productivity
* ⚡ Faster and smarter HR decisions

---

## ⚙ Tech Stack

* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-learn (Logistic Regression, Random Forest)
* **Visualization:** Matplotlib, Seaborn
* **Dashboard:** Streamlit
* **Model Storage:** Joblib

---

## 📊 Dataset

Synthetic Employee Dataset

### Features:

* age
* experience_years
* department
* salary
* training_hours
* projects_completed
* attendance_rate
* manager_feedback
* overtime_hours

### Target:

* `performance_rating` → (High / Medium / Low)

---

## 🏗 System Architecture

```
Raw Data → Preprocessing → Feature Engineering → ML Model → Prediction → Insights → Dashboard
```

---

## 📁 Project Structure

```
EMPLOYEE-PERFORMANCE-PREDICTOR/
├── app/
│   └── app.py
├── data/
│   ├── employee_data.csv
│   └── test.csv
├── images/
│   ├── phase1/
│   ├── phase2/
│   ├── phase3/
│   ├── phase4/
│   ├── phase5/
│   ├── phase6/
│   └── Video Project 2.mp4
├── models/
│   └── model.pkl
├── notebooks/
│   └── eda.ipynb
├── output/
├── src/
│   ├── data_processing/
│   ├── model/
│   └── utils/
├── venv/
├── main.py
├── README.md
└── requirements.txt
```

---

## ⚙ Installation & Setup

```
git clone https://github.com/maheshbhakre/employee-performance-predictor.git
cd employee-performance-predictor

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

---

## 🖥 Usage

```
# Run model training (optional)
python main.py

# Run dashboard
streamlit run app/app.py
```

---

## 📊 Model Performance

* Accuracy: ~90%
* Macro F1 Score: ~0.80+
* Balanced using SMOTE
* Random Forest used for final predictions

---

## 📸 PHASE-WISE IMPLEMENTATION PROOF

### 🔹 Phase 1

![P1](images/phase1/Screenshot%202026-04-18%20002216.png)
![P1](images/phase1/Screenshot%202026-04-18%20002247.png)

### 🔹 Phase 2

![P2](images/phase2/Screenshot%202026-04-18%20002302.png)

### 🔹 Phase 3

![P3](images/phase3/Screenshot%202026-04-18%20002651.png)

### 🔹 Phase 4

![P4](images/phase4/Screenshot%202026-04-18%20010202.png)

### 🔹 Phase 5

![P5](images/phase5/Screenshot%202026-04-18%20010524.png)

### 🔹 Phase 6

![P6](images/phase6/Screenshot%202026-04-18%20010734.png)

---

## 🧠 Key Insights

* Manager feedback is the strongest predictor
* Training hours significantly impact performance
* Attendance and project completion affect outcomes
* Overtime alone does not guarantee high performance

---

## 👨‍💻 Author

Mahesh Bhakre

---

## 🌐 CONNECT WITH ME

<a href="https://github.com/maheshbhakre">
<img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github">
</a>

<a href="https://www.linkedin.com/in/maheshbhakreds1242">
<img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin">
</a>

<a href="https://www.instagram.com/mahesh_bhakre__2k06">
<img src="https://img.shields.io/badge/Instagram-Follow-purple?style=for-the-badge&logo=instagram">
</a>

<a href="https://saimfsd.github.io/mahesh-portfolio/">
<img src="https://img.shields.io/badge/Portfolio-Visit%20Website-orange?style=for-the-badge&logo=google-chrome">
</a>

---

## ⭐ NOTE

This project demonstrates a complete **end-to-end AI-powered HR analytics system**, covering:

* Data generation
* Data analysis (EDA)
* Machine learning modeling
* Performance prediction
* Dashboard deployment

---

## 🚀 Future Improvements

* Add real HR dataset
* Build deep learning model
* Add employee attrition prediction
* Deploy on cloud (AWS / Azure)
* Add real-time API

---

## 🎯 Interview Tip

Explain your project like this:

> “I built an AI-based employee performance prediction system using machine learning.
> It predicts employee performance levels and helps HR teams make data-driven decisions.
> I implemented end-to-end pipeline including data generation, EDA, model training, and a live dashboard.”

---
