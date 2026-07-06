# Big Data Analytics with Hadoop and Spark
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.x-E25A1C?logo=apachespark)
![PySpark](https://img.shields.io/badge/PySpark-Data%20Processing-orange)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black?logo=github)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

##  Project Overview

This project demonstrates the use of **Apache Spark (PySpark)** for processing and analyzing large-scale agricultural datasets from Kenya.

The objective is to build a scalable analytics workflow that performs data loading, cleaning, transformation, and statistical analysis using distributed computing principles.

The project showcases how Spark can efficiently process structured datasets while uncovering trends in Kenya's agricultural production over time.

---

##  Project Objectives

- Load a Kenyan agricultural dataset into Apache Spark.
- Clean and preprocess the data.
- Perform Spark transformations.
- Compute descriptive statistics and aggregations.
- Identify trends and outliers.
- Produce insights through visualizations and reporting.
- Demonstrate collaborative development using Git and GitHub.

---

#  Project Structure

```
Big-Data-Analytics-with-Hadoop-and-Spark
│
├── data
│   ├── raw
│   │   └── kenya_agriculture_raw.csv
│   │
│   ├── processed
│   │
│   └── outputs
│
├── notebooks
│   └── kenya_agriculture.ipynb
│
├── scripts
│   ├── load_data.py
│   ├── transformations.py
│   ├── analysis.py
│   └── main.py
│
├── reports
│   └── Final_Report.pdf
│
├── images
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

#  Dataset

**Source**

FAOSTAT Kenya Agricultural Production Dataset

The dataset contains agricultural production statistics including:

- Area harvested
- Crop production
- Yield
- Agricultural products
- Units of measurement
- Time series data

---

#  Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming |
| Apache Spark | Distributed Data Processing |
| PySpark | Spark API |
| Pandas | Exploratory Analysis |
| Jupyter Notebook | Development |
| Git | Version Control |
| GitHub | Collaboration |

---

#  Getting Started

## Clone the repository

```bash
git clone https://github.com/Hmati/Big-Data-Analytics-with-Hadoop-and-Spark.git

cd Big-Data-Analytics-with-Hadoop-and-Spark
```

---

## Create a virtual environment

Windows

```bash
python -m venv spark_env
```

Activate

```bash
spark_env\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv spark_env

source spark_env/bin/activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the project

Run the notebook

```bash
jupyter notebook
```

OR execute the scripts

```bash
python scripts/main.py
```

---

# 🔄 Workflow

```
Kenya Agricultural Dataset
            │
            ▼
      Data Loading
            │
            ▼
      Data Cleaning
            │
            ▼
   Spark Transformations
            │
            ▼
   Analytics & Statistics
            │
            ▼
     Insights & Report
```

---

#  Analysis Performed

The project explores:

- Crop production trends
- Average production by crop
- Area harvested over time
- Highest producing crops
- Year-over-year comparisons
- Outlier detection
- Descriptive statistics

---

#  Sample Spark Operations

Examples include:

- Data Filtering
- GroupBy Operations
- Aggregations
- Average Calculations
- Sorting
- Column Transformations
- Null Handling

---

#  Team Collaboration

The project follows a Git feature-branch workflow.

| Branch | Responsibility |
|---------|----------------|
| main | Production-ready code |
| develop | Integration branch |
| feature-data-loading | Data ingestion |
| feature-data-cleaning | Data preprocessing |
| feature-transformations | Spark transformations |
| feature-analysis | Analytics |
| feature-report | Documentation |

---

#  Key Learning Outcomes

- Distributed data processing with Apache Spark
- Big Data ETL workflows
- Data cleaning using Spark
- Spark DataFrame transformations
- Git collaboration
- Data storytelling
- Statistical analysis

---

#  Sample Outputs

Project visualizations and screenshots will be added in the **images/** folder.

---

#  Future Improvements

- Hadoop HDFS integration
- Spark SQL
- Machine Learning with MLlib
- Airflow orchestration
- Power BI dashboard
- Docker containerization

---
