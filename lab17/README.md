# Lab 17: Extract Patterns Using Regular Expressions

## Project Overview

This project demonstrates how to use **Regular Expressions (Regex)** in Python to extract, clean, and standardize messy text data commonly found in real-world healthcare records.

Using **Python, Pandas, and Regex**, the notebook processes patient records to extract structured information such as:

* Patient names
* Ages
* Phone numbers
* Addresses
* Patient IDs
* Appointment dates and years

The goal of this lab is to practice **data cleaning and pattern extraction techniques**, which are essential skills for **data analysts and data scientists**.

---

## Objectives

By completing this lab, the following skills were developed:

* Understand the fundamentals of **Regular Expressions (Regex)**
* Use **Pandas `str.extract()`** to extract structured information from messy text
* Clean and standardize **address fields and patient IDs**
* Extract **years from multiple date formats**
* Apply regex techniques to **real-world healthcare data scenarios**

---

## Technologies Used

* Python
* Pandas
* NumPy
* Regular Expressions (`re`)
* Matplotlib (for visualization)
* Jupyter Notebook

---

## Tasks Performed

### Task 1: Extract Data from Messy Patient Records

Used regex patterns with `str.extract()` to retrieve:

* Patient names
* Patient ages
* Phone numbers in multiple formats

### Task 2: Clean Address and ID Fields

Applied regex replacement techniques to:

* Remove extra spaces in addresses
* Standardize address formatting
* Clean inconsistent patient ID formats
* Extract ID number and location code

### Task 3: Extract Year from Date Strings

Handled multiple date formats such as:

* `YYYY-MM-DD`
* `MM/DD/YYYY`
* `Month DD, YYYY`

Extracted and analyzed year information from appointment records.

---

## Data Visualization

Basic visualizations were created to better understand the dataset:

* Patient Age Distribution
* Appointments by Year
* Patient Age Comparison

These visualizations help highlight patterns within the cleaned dataset.

---

## Project Structure

```
regex-data-cleaning-lab
│
├── Lab17_Regex_Data_Cleaning.ipynb
└── README.md
```

---

## Example Regex Patterns Used

Extract patient names:

```python
name_pattern = r'(?:Patient:|Name:|Patient Name:)\s*([A-Za-z\s]+?)(?:,|\s-\sAge|\sAge)'
```

Extract ages:

```python
age_pattern = r'Age:?\s*(\d+)'
```

Extract phone numbers:

```python
phone_pattern = r'(?:Phone:|Tel:|Contact:|Phone Number:)\s*(\(?[\d]{3}\)?[-.\s]?[\d]{3}[-.\s]?[\d]{4})'
```

---

## Key Learning Outcomes

* Handling messy real-world datasets
* Writing flexible regex patterns
* Extracting structured information from unstructured text
* Cleaning inconsistent data formats
* Building reproducible data-cleaning workflows

---

## Author

Created by: **Muhammad Akhtar**

This project is part of a **Data Science / Data Analysis learning lab** focused on practical regex applications.

---

## License

This project is created for **educational purposes**.
