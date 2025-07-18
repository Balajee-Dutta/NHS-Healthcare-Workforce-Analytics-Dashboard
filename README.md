
# NHS Healthcare Workforce Analytics Dashboard

Welcome to the NHS Healthcare Workforce Analytics Dashboard! This project provides an end-to-end solution for analyzing HR data, predicting attrition risk using machine learning, and visualizing key workforce metrics in an interactive Power BI dashboard.

---

## 📖 Table of Contents

1. [Project Overview](#project-overview)
2. [Repository Structure](#repository-structure)
3. [Prerequisites](#prerequisites)
4. [Setup & Installation](#setup--installation)
5. [Data Sources](#data-sources)
6. [Python Script: Attrition Risk Analysis](#python-script-attrition-risk-analysis)
7. [Interactive Dashboard (Power BI)](#interactive-dashboard-power-bi)
8. [Usage](#usage)
9. [Extending & Customization](#extending--customization)
10. [Contributing](#contributing)
11. [License](#license)
12. [Contact](#contact)

---

## 🚀 Project Overview

This repository showcases an HR analytics workflow for the NHS UK. It includes:

* **Data preparation**: Cleans and encodes employee records from Excel.
* **Attrition prediction**: Trains Logistic Regression and Random Forest models to estimate each employee's likelihood of leaving (attrition risk).
* **Risk scoring**: Appends a continuous `AttritionRisk` score for each record.
* **Visualization**: Combines the enriched dataset with historical headcount, absenteeism, and other HR KPIs in a Power BI dashboard.

Use this solution to:

* Identify high-risk employees before they leave.
* Track workforce trends and KPIs over time.
* Enable data-driven HR decision making.

---

## 📂 Repository Structure

```bash
├── data/
│   ├── NHS Attrition Data_UK.xlsx          # Raw HR attrition dataset
│   ├── NHS_Attrition_Data_with_Risk.xlsx   # Output from attrition script
│   ├── Additional_HR_Metrics_1.xlsx        # Supplementary workforce metrics
│   ├── Additional_HR_Metrics_2.xlsx
│   ├── ...
├── src/
│   └── attrition_risk_analysis.py          # Python script for data prep & modeling
├── dashboard/
│   └── NHS_HR_Workforce_Dashboard.pbix     # Power BI report file
├── requirements.txt                        # Python dependencies
├── README.md                               # This file
└── LICENSE                                 # Project license
```

---

## ⚙️ Prerequisites

* **Python 3.8+**
* **Power BI Desktop** (for `.pbix` file)
* **Git** (to clone this repo)

---

## 🛠️ Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Balajee-Dutta/NHS-Healthcare-Workforce-Analytics-Dashboard.git
   cd NHS-Healthcare-Workforce-Analytics-Dashboard
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate         # macOS/Linux
   venv\Scripts\activate.bat      # Windows
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Place your data files** in the `data/` directory. Ensure the raw attrition file is named exactly:

   ```
   ```

data/NHS Attrition Data\_UK.xlsx

````

---

## 📊 Data Sources

- **`data/NHS Attrition Data_UK.xlsx`**: Historical HR records, including demographics, job roles, tenure, and attrition flag.
- **`data/Additional_HR_Metrics_*.xlsx`**: Other workforce metrics (e.g., absenteeism, headcount by department, training hours).
- **`data/NHS_Attrition_Data_with_Risk.xlsx`**: Generated output with appended `AttritionRisk` scores ready for dashboard ingestion.

---

## 🐍 Python Script: Attrition Risk Analysis

**File**: `src/attrition_risk_analysis.py`

This script performs:

1. **Data loading** from Excel.
2. **One-hot encoding** of categorical features.
3. **Train/test split** (70% train, 30% test, stratified).
4. **Model training**: Logistic Regression and Random Forest.
5. **Evaluation**: Classification reports & ROC-AUC scores printed to console.
6. **Risk score assignment**: Appends `AttritionRisk` probability for each employee.
7. **Export**: Saves enriched dataset to `data/NHS_Attrition_Data_with_Risk.xlsx`.

### Running the script

```bash
python src/attrition_risk_analysis.py
````

Check the console for performance metrics and confirm the output Excel file in `data/`.

---

## 📈 Interactive Dashboard (Power BI)

**File**: `dashboard/NHS_HR_Workforce_Dashboard.pbix`

Open this file in Power BI Desktop to explore:

* Attrition risk distribution by department, tenure, and demographic segments.
* Time-series of headcount, new hires, and exits.
* Drill-through from summary charts to individual employee risk profiles.

Ensure that Power BI is pointed at the updated `NHS_Attrition_Data_with_Risk.xlsx` and any other metric files in `data/`.

---

## 🔧 Usage

1. **Generate latest risk scores**

   ```bash
   python src/attrition_risk_analysis.py
   ```
2. **Refresh Power BI Dashboard**

   * Open `dashboard/NHS_HR_Workforce_Dashboard.pbix`.
   * Click **Refresh** to load updated Excel data.
3. **Publish** (optional)

   * Save your changes and publish to Power BI Service for broader sharing.

---

## ✨ Extending & Customization

* **Add new features**: Update `attrition_risk_analysis.py` to include additional predictors (e.g., training hours, performance ratings).
* **Tune models**: Experiment with hyperparameters or alternative algorithms (XGBoost, LightGBM).
* **Data pipeline**: Automate data ingestion using Power Query or Azure Data Factory.
* **Security & governance**: Integrate with Azure AD and row-level security in Power BI.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repo.
2. Create a feature branch: `git checkout -b feature/my-change`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to your branch: `git push origin feature/my-change`
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 📬 Contact

For questions or feedback, please open an issue or contact:

* **Balajee Dutta** (Maintainer)
* Email: [bldutta94@gmail.com](mailto:bldutta94@gmail.com)

Happy analyzing! 🎉
