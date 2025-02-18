# data-science-campus-recruitment

# Project Overview
This project analyzes student placement data to uncover insights related to academic performance, work experience, and placement outcomes. It includes data preprocessing, exploratory data analysis (EDA), visualizations, and machine learning modeling to predict placement status.

# Folder Structure
```
project-root/
├── data/            # Raw dataset
├── scripts/         # Python scripts for analysis
├── outputs/         # Generated results and models
├── requirements.txt # Required dependencies
└── README.md        # Project documentation
```

# Usage

## 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file:
```bash
pip install -r requirements.txt
```

## 2. Run Preprocessing Script
Cleans and prepares the data.
```bash
python scripts/01_preprocessing.py
```

## 3. Run Exploratory Data Analysis (EDA) Script
Generates summary statistics and categorical distributions.
```bash
python scripts/02_eda.py
```

## 4. Run Visualization Script
Creates histograms, bar plots, and correlation heatmaps.
```bash
python scripts/03_visualization.py
```

## 5. Run Machine Learning Model
Trains a Random Forest model to predict placement status and evaluates performance.
```bash
python scripts/04_modeling.py
```

# Requirements
- Python 3.x
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- joblib

# Acknowledgments
**Dataset Name:** Campus Recruitment  
**Dataset Author:** Ben Roshan  
**Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/benroshan/factors-affecting-campus-placement/)
