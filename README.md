# Vendor Performance Analysis

## Project Overview

Vendor Performance Analysis is an end-to-end data analytics project that analyses vendor sales, purchasing, profitability, inventory turnover, and brand performance.

The project uses Python, SQL, SQLite, Jupyter Notebook, and Power BI to transform raw vendor data into a consolidated analytical dataset, perform exploratory data analysis, and develop an interactive dashboard.

## Project Objectives

- Analyse vendor sales and purchasing performance.
- Identify top-performing vendors based on sales.
- Identify top-performing brands based on sales.
- Analyse vendor profitability and profit margins.
- Analyse purchase contribution across vendors.
- Evaluate inventory turnover.
- Identify low-performing vendors and brands.
- Develop an interactive Power BI dashboard.
- Generate business insights and recommendations from the analysis.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQL
- SQLite
- Jupyter Notebook
- SciPy
- Power BI
- Git and GitHub

## Project Workflow

```text
Raw CSV Files
      ↓
Data Ingestion
      ↓
SQLite Database
      ↓
SQL Vendor Summary
      ↓
Data Cleaning & Feature Engineering
      ↓
Exploratory Data Analysis
      ↓
Statistical Analysis
      ↓
Power BI Dashboard
      ↓
Business Insights & Recommendations

 
 ## Dataset
The project uses the following datasets:

Beginning Inventory
Ending Inventory
Purchase Prices
Purchases
Sales
Vendor Invoice

These datasets are combined and transformed to create a consolidated vendor_sales_summary dataset.

Data Preparation

The project includes:

Loading CSV files using Pandas
Inspecting the datasets
Cleaning and preparing the data
Combining vendor, sales, purchase, and inventory information
Creating the vendor sales summary
Creating additional business metrics
Feature Engineering

The following metrics were created during the analysis:

Gross Profit
Profit Margin
Stock Turnover
Sales-to-Purchase Ratio
Total Sales Quantity
Total Purchase Quantity
Total Sales Dollars
Total Purchase Dollars
Freight Cost



## Exploratory Data Analysis

Exploratory Data Analysis was performed using Python and Jupyter Notebook.

The analysis focused on:

Vendor performance
Brand performance
Sales distribution
Purchase distribution
Profitability
Profit margins
Inventory turnover
Relationships between business metrics
Identification of potential outliers

Statistical analysis and hypothesis testing were also performed as part of the project.

Power BI Dashboard

An interactive Power BI dashboard was developed to provide a visual overview of vendor and brand performance.

### Key KPIs

Total Sales: $441.41M
Total Purchase: $307.34M
Gross Profit: $134.07M
Profit Margin: 38.72%
Unsold Capital: $2.71M

Dashboard Visuals

Purchase Contribution by Vendor
Top Vendors by Sales
Top Brands by Sales
Low Performing Vendors
Top Brands by gross profit.

Key Business Insights
The dashboard highlights vendors contributing significantly to total purchases.
Top vendors and brands can be identified based on sales performance.
Vendor profitability can be evaluated using gross profit and profit margin.
Stock turnover helps identify vendors with slower-moving inventory.
Brands with relatively lower sales and higher profit margins can be further investigated for business opportunities.
Unsold inventory represents capital that may require better inventory planning.


Business Recommendations
Monitor vendors with low stock turnover.
Review inventory levels to reduce unsold capital.
Analyse low-sales brands with higher profit margins for potential growth opportunities.
Monitor vendor performance using sales, profitability, and inventory metrics together.
Review purchasing patterns to improve inventory planning.
Use dashboard insights to support data-driven business decisions.


    **Project Structure**
Vendor-Performance-Analysis/
│
├── data/
│   ├── beginning_inventory.csv
│   ├── end_inventory.csv
│   ├── purchase_prices.csv
│   ├── purchases.csv
│   ├── sales.csv
│   └── vendor_invoice.csv
│
├── logs/
│
├── data_analysis.ipynb
├── exploratory_Analysis.ipynb
├── Vendor Performance Analysis.ipynb
│
├── ingestion_db.py
├── get_vendor_summary.py
│
├── inventory.db
├── vendor_sales_summary.csv
│
├── vendor Performance Dashboard.pbix
├── Vendor Performance Analysis Report.docx
│
├── README.md
└── .gitignore



How to Run the Project
1. Clone the Repository
git clone https://github.com/Samatha-chigurla/Vendor-Performance-Dashoboard

2. Open the Project
cd Vendor-Performance-Analysis

3. Install Required Libraries
pip install pandas, numpy, matplotlib, seaborn, scipy, sqlalchemy jupyter

4. Run Data Ingestion
python ingestion_db.py

5. Generate Vendor Summary
python get_vendor_summary.py

6. Open Jupyter Notebook
jupyter notebook

Open the required notebook and run the analysis.

7. Open the Power BI Dashboard

Open the .pbix file using Power BI Desktop.

Project Outcome

This project demonstrates an end-to-end data analytics workflow starting from raw data ingestion and SQL-based data processing through Python-based exploratory analysis, statistical analysis, Power BI visualisation, and business reporting.

The project demonstrates practical skills in:

Data Cleaning
Python
SQL
SQLite
Exploratory Data Analysis
Statistical Analysis
Power BI
Dashboard Development
Business Reporting

Author
Samatha Chigurla
