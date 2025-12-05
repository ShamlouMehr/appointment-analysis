# Ambulatory Access & Utilization Dashboard  
### **A Decision Support Analytics Project by Ahmad ShamlouMehr**

---

## Overview  
This project demonstrates an **end-to-end analytics workflow** designed to support patient access, appointment utilization, and operational decision-making in an ambulatory healthcare environment.

It includes:

- Data cleaning & preparation  
- Access and utilization metrics  
- Scheduling and no-show analysis  
- Capacity vs. demand visualization  
- Anomaly detection  
- A Streamlit dashboard for interactive exploration  

This work is modeled after the responsibilities of a **Decision Support Analyst** at major healthcare systems, including teams at **Nationwide Children’s Hospital**.

---

## Objectives  
The analysis and dashboard aim to:

- Provide clear, actionable insights into *patient access*  
- Identify utilization patterns, bottlenecks, and scheduling inefficiencies  
- Detect anomalies or unexpected changes in appointment behavior  
- Support operational leaders in making data-driven decisions  
- Demonstrate technical skills in analytics, visualization, and reporting  

---

## Technology Stack  
- **Python** (Pandas, NumPy)  
- **Streamlit** (interactive dashboard)  
- **Plotly / Matplotlib** (visualization)  
- **Scikit-learn** (optional anomaly detection)  
- **GitHub** for version control and documentation  

---

## Features  

### **1. KPI Summary Cards**  
- Fill rate  
- No-show rate  
- Cancellation rate  
- Average lead time  
- Capacity vs. scheduled demand  

### **2. Interactive Visualizations**  
- Capacity vs. demand line charts  
- No-show and cancellation breakdowns  
- Provider- or clinic-level utilization  
- Scheduling frequency heatmaps (hour/day)  

### **3. Anomaly Detection**  
Simple rolling-mean anomaly flagging to surface unusual utilization drops or spikes:

```python
df["is_anomaly"] = df["utilization"] < df["utilization"].rolling(7).mean() * 0.7
```



### **4. Data Quality & Validation Checks**
Ensures reliability of scheduling and utilization data:
- Missing values  
- Invalid or future dates  
- Duplicate appointments  
- Out-of-range or inconsistent values  

### **5. Filtering Options**
Interactive filters built into the dashboard:
- Clinic / Specialty  
- Provider  
- Appointment type  
- Date range  



## How to Run the Dashboard  

### **1. Clone the repository**
```bash
git clone https://github.com/ShamlouMehr/appointment-analysis.git
```
### 2. Install dependencies**
```bash
pip install -r requirements.txt
```
### 3. Run Streamlit**
```bash
streamlit run app.py
```
The dashboard will open automatically in your browser.



