# 🏦 Banking Branch Performance Analytics
### Banking Deposit Distribution, Institutional Rankings, and Market Concentration

## 🚀 Live Interactive Dashboard

**[Open the live Streamlit dashboard](https://bankingbranchperformanceanalytics-iznjueoncuiuwqdqjl6wey.streamlit.app/)**

This project develops an interactive business analytics dashboard using the Federal Deposit Insurance Corporation (FDIC) *Summary of Deposits* data.

The objective is to analyze the geographic distribution of bank deposits, compare financial institutions, assess market concentration, investigate deposit distributions and data quality, and translate statistical findings into actionable business recommendations.

## 🎯 Project Objectives

- Analyze bank deposit distribution across U.S. states.
- Identify financial institutions with the largest aggregated deposit balances.
- Measure market concentration using the Herfindahl-Hirschman Index (HHI).
- Examine the combined market share of the three largest institutions in each state.
- Investigate zero-deposit records and extreme observations.
- Compare states using multiple business indicators.
- Develop data-driven recommendations while acknowledging analytical limitations.

## 📊 Key Features

### 1. Descriptive Analytics
- Key performance indicators: total deposits, number of institutions, office records, and states.
- State-level deposit rankings.
- Financial institution rankings based on aggregated deposits.

### 2. Market Concentration Analysis
- State-level HHI calculations.
- Top-three institution deposit shares.
- Comparisons of market concentration across states.
- Identification of markets requiring further investigation.

### 3. Deposit Distribution and Data Quality
- Identification of records with zero deposits.
- Comparison of deposit distributions by branch number.
- Boxplot visualization of deposit values and extreme observations.
- Review of the largest individual office records.

### 4. State Comparison and Business Recommendations
- Comparison of total deposits, institution counts, office records, and median deposits.
- Interactive visualization of relationships between business indicators.
- Analytical recommendations based on observed concentration patterns.

## 🧰 Technology Stack

- **Python** — data analysis and processing.
- **Pandas** — data cleaning, aggregation, and manipulation.
- **Plotly Express** — interactive visualizations.
- **Streamlit** — dashboard development and deployment.
- **Pathlib** — file path management.

## 📁 Data Source

The dataset comes from the FDIC *Summary of Deposits* program.

Official source: [FDIC — Summary of Deposits](https://www.fdic.gov/bank-data-guidebank/summary-deposits-sod)

The dataset includes financial institution identifiers, office locations, state information, office identifiers, and deposit balances.

The source field `DEPSUMBR` is expressed in thousands of dollars and is converted to billions of dollars for selected dashboard visualizations.

## 📈 Analytical Methods and Metrics

### Herfindahl-Hirschman Index (HHI)

The HHI is calculated by summing the squared market shares, expressed as percentages:

\[
HHI = \sum_{i=1}^{N} s_i^2
\]

where \(s_i\) is institution \(i\)'s share of total deposits in a given state.

The project uses the following descriptive screening categories:

- **HHI below 1,500:** relatively low concentration.
- **HHI from 1,500 to 2,500:** moderate concentration.
- **HHI above 2,500:** high concentration.

These categories support exploratory analysis and should not be interpreted as definitive regulatory findings about competition.

### Additional Metrics

- Total deposits by state and institution.
- Combined deposit share of the three largest institutions.
- Number of institutions and office records.
- Mean and median deposit balances.
- Number of zero-deposit records.

## 💡 Key Analytical Insights

The analysis highlights several important aspects of the U.S. banking market:

- Deposit volumes differ substantially across states.
- Some state markets have deposits concentrated among a relatively small number of institutions.
- Extremely large observations can affect averages, making median values useful for comparison.
- Zero-deposit records require investigation before operational conclusions are drawn.
- Larger deposit balances do not necessarily indicate higher profitability or operational efficiency.

## 🧭 Business Recommendations

1. **Monitor deposit concentration** in states where a small number of institutions hold a large share of deposits.
2. **Compare states using multiple indicators**, rather than relying on total deposits alone.
3. **Investigate zero and extreme deposit values** to distinguish potential data issues from legitimate observations.
4. **Track market shares over time** to identify changes in concentration and market structure.
5. **Enrich the dataset** with operating costs, customer counts, loan balances, transaction volumes, and revenue to support a more complete assessment of branch performance.

## ⚠️ Limitations

- The analysis uses a single dataset extract and does not, by itself, establish time trends.
- Deposit balances do not directly measure profitability or operational efficiency.
- The operational meaning of certain branch-number values should be verified before interpretation.
- State-level HHI may conceal differences between local banking markets.
- Concentration categories are descriptive screening indicators, not regulatory conclusions.

## ▶️ Run the Project Locally

1. Clone the GitHub repository.
2. Install the required dependencies.
3. Place the CSV dataset in the project directory.
4. Launch the Streamlit application.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Banking-Branch-Performance-Analytics
pip install -r requirements.txt
streamlit run app.py
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the actual repository URL.

## 📂 Project Structure

```text
Banking-Branch-Performance-Analytics/
├── app.py
├── requirements.txt
├── SOD_CustomDownload_2026_06_30 (1).csv
└── README.md
```

## 👨‍💻 Author

** Nymbussede Leny  Napala**

Business Analytics and applied data analysis portfolio project focused on banking data.

🔗 [Explore the live dashboard](https://bankingbranchperformanceanalytics-iznjueoncuiuwqdqjl6wey.streamlit.app/)
