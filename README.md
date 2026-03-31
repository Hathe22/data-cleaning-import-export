# Import Export Data Cleaning Project

## 1. Project Overview
This project aims to clean and standardize raw import-export Excel data to create a clean dataset ready for analysis and visualization.

The project simulates a real-world Data Analyst workflow, including data understanding, data cleaning, data mapping, data validation, and data preparation for dashboards.

## 2. Data Pipeline
Raw Excel Data → Data Understanding → Data Cleaning → Data Mapping → Data Validation → Clean Data → Dashboard

## 3. Project Structure
data/
    raw/        # Raw data (ignored by git)
    clean/      # Clean data (ignored by git)
    master/     # Master data (product list, country mapping)

src/
    clean.py
    mapping.py
    validate.py
    main.py

docs/
    data_dictionary.xlsx
    business_rules.xlsx
    data_issues.xlsx

output/
    final_clean.xlsx

## 4. Technologies Used
- Python (Pandas, NumPy)
- Excel
- GitHub
- Power BI / Excel Dashboard

## 5. Team Members
- Thế – Team Leader – Data Cleaning Pipeline
- Tuấn – Data Mapping & Master Data
- Hưng – Data Validation & Business Rules

## 6. Project Output
- Data Dictionary
- Business Rules
- Clean Excel Dataset
- Data Cleaning Python Scripts
- Dashboard for Import-Export Analysis
