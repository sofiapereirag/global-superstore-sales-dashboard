# Global Superstore Interactive Sales Dashboard

Turn raw sales data into interactive insights — fast, clean, and visual.

An interactive sales dashboard built with **Streamlit** using the [Global Superstore dataset](https://www.kaggle.com/datasets/fatihilhan/global-superstore-dataset).  
This project demonstrates **data analysis, preprocessing, and interactive visualization** for sales data.

---



## Live Demo
You can try the live version hosted on Streamlit Cloud:
https://global-superstore-sales-dashboard-bksthqnyeavkjkfgwanrbh.streamlit.app/

---


## Features

- **Interactive filters** for year and region
- **Key metrics**: Total Sales, Total Profit, Number of Orders
- **Dynamic visualizations**:
  - Sales by Category
  - Profit by Region
  - Sales Over Time
- Clean and modular code structure with separate functions for:
  - Data loading
  - Data visualization
  - Utility formatting

---

## Repository Structure

sales-dashboard
- data/
  - processed/ # Cleaned dataset
- notebooks/
  - 01_eda.ipynb # Exploratory Data Analysis
  - 02_preprocessing.ipynb # Data cleaning and preprocessing
- src/
  - app.py # Main Streamlit application
  - data_loader.py # Functions to load and prepare data
  - plots.py # Functions to generate plots
  - utils.py # Utility functions
- README.md
- requirements.txt


---

## 🛠 Tech Stack

- **Python**: Data analysis and scripting
- **Pandas**: Data manipulation
- **Plotly**: Interactive visualizations
- **Streamlit**: Web app framework
- **Matplotlib & Seaborn**: Static plots for EDA
- **Jupyter Notebook**: EDA and preprocessing

---


## Dataset

The dataset contains sales data from a global retail store, including:

- Order and shipping dates
- Product categories and sub-categories
- Sales, profit, discount, and quantity
- Customer segments and regions

Source: [Kaggle - Global Superstore Dataset](https://www.kaggle.com/datasets/fatihilhan/global-superstore-dataset)

---

##  How to Run

### 1. Clone the repository
git clone https://github.com/your-username/sales-dashboard.git
cd sales-dashboard
### 2. Install dependencies
pip install -r requirements.txt
### 3. Run the app
streamlit run app/dashboard.py

---

## Project Workflow
1.Exploratory Data Analysis (EDA)
- Understand the dataset structure
- Identify trends, patterns, and data quality issues
- Generate initial insights

2. Data Preprocessing
- Fix missing values and inconsistent dates
- Remove extreme outliers
- Create new features (Year, Month, Profit Margin)
- Save cleaned dataset

3. Dashboard Development
- Modularize code into separate .py files
- Implement interactive filters
- Create dynamic KPIs and visualizations


---


## Future Improvements
- Add sales forecasting using machine learning

- Include customer segmentation analysis

- Enable CSV export of filtered data


---


## Author
Sofia Gonçalves
Master’s student in Electrical and Computer Engineering — Networks & Telecommunications
Skills: Python, Data Analysis, Machine Learning, Data Visualization





