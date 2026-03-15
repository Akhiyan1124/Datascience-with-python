# Lab 18: Clean and Analyze EMR Patient Data

## 📌 Project Overview
This project demonstrates a complete healthcare data analysis workflow using simulated **Electronic Medical Record (EMR)** datasets from multiple hospitals.  

The goal of this lab is to practice real-world **data cleaning, merging, filtering, and statistical analysis** using Python and the Pandas library.

Healthcare datasets are often messy and inconsistent. This project shows how data analysts prepare such datasets before performing meaningful analysis.

---

## 🎯 Learning Objectives

By completing this lab, the following skills were developed:

- Clean and merge multiple hospital EMR datasets
- Remove duplicate patient records
- Standardize column names for analysis
- Filter patient data based on diagnosis
- Perform statistical analysis on patient outcomes
- Calculate average hospital length of stay
- Use Python Pandas for healthcare data analytics

---

## 📂 Dataset

The project uses **three simulated hospital datasets**:

- `hospital_a_patients.csv`
- `hospital_b_patients.csv`
- `hospital_c_patients.csv`

Each dataset contains the following columns:

| Column | Description |
|------|-------------|
| patient_id | Unique patient identifier |
| patient_name | Patient name |
| diagnosis | Medical diagnosis |
| outcome | Patient outcome |
| length_of_stay | Number of days patient stayed in hospital |

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

## 📊 Project Workflow

### 1️⃣ Data Loading
Load EMR datasets from multiple hospitals.

### 2️⃣ Data Cleaning
Standardize column names and fix formatting issues.

### 3️⃣ Dataset Merging
Combine multiple hospital datasets into one unified dataset.

### 4️⃣ Duplicate Removal
Identify and remove duplicate patient records.

### 5️⃣ Data Filtering
Filter patient records based on specific diagnoses.

### 6️⃣ Data Analysis
Analyze patient outcomes and compute statistical measures such as:

- Average length of stay
- Median stay duration
- Minimum and maximum stay

### 7️⃣ Results Export
Save analysis results into CSV files.

---

## 📈 Example Analysis

The project analyzes **average hospital stay based on patient outcomes**, helping identify patterns such as:

- Patients with certain outcomes having longer hospital stays
- Differences between diagnosis categories

---

## 📁 Repository Structure

```
lab18-emr-analysis
│
├── lab18_emr_analysis.ipynb
├── hospital_a_patients.csv
├── hospital_b_patients.csv
├── hospital_c_patients.csv
└── README.md
```

---

## 🚀 How to Run the Project

1. Clone this repository

```
git clone https://github.com/yourusername/lab18-emr-analysis.git
```

2. Install required libraries

```
pip install pandas numpy matplotlib
```

3. Open the notebook

```
jupyter notebook lab18_emr_analysis.ipynb
```

---

## 📊 Sample Output

The project generates analysis such as:

- Average hospital stay by patient outcome
- Diagnosis distribution
- Outcome statistics

Results are saved in:

- `emr_outcome_analysis.csv`
- `emr_detailed_analysis.csv`

---

## 📚 Learning Outcome

This project demonstrates essential **data preprocessing and analysis techniques used in healthcare analytics**, including:

- Data integration
- Data cleaning
- Duplicate handling
- Statistical analysis
- Data-driven insights

These skills are highly valuable in **data science, healthcare analytics, and medical informatics**.

---

## 👨‍💻 Author

Muhammad Akhtar

Data Science | Cybersecurity | Python

---

## ⭐ If you found this project useful

Please consider **starring this repository** on GitHub.
