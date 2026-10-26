# BANKING_BRANCH_PERFORMANCE_ANALYTICS
# 🏦 Banking Branch Performance Analytics
## 🚀 Live Dashboard

**Explore the interactive dashboard:** [Banking Branch Performance Analytics](https://bankingbranchperformanceanalytics-iznjueoncuiuwqdqjl6wey.streamlit.app/)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bankingbranchperformanceanalytics-iznjueoncuiuwqdqjl6wey.streamlit.app/)

Analyze banking deposit distribution, compare institutions and states, investigate market concentration, and explore business recommendations through an interactive Streamlit dashboard.


## 📌 Project Overview

This project analyzes the **FDIC Summary of Deposits (SOD)** dataset to explore deposit distribution across U.S. banking institutions and states. It applies data analysis, statistical methods, and business analytics techniques to identify deposit concentration patterns, compare geographic markets, and investigate differences in reported deposit balances.

The objective is to transform banking data into actionable business insights that can support market analysis, strategic planning, and further investigation of banking network performance.

## 🎯 Business Objectives

- Analyze the distribution of bank deposits across U.S. states.
- Identify the largest banking institutions by total deposits.
- Measure deposit concentration using the Herfindahl-Hirschman Index (HHI).
- Compare the combined deposit share of the three largest institutions in selected states.
- Examine deposit distributions and detect unusually large observations.
- Translate analytical findings into practical business recommendations.

## 📊 Dataset

**Source:** Federal Deposit Insurance Corporation (FDIC) — Summary of Deposits (SOD).

The dataset contains information about banking offices, institutions, geographic locations, and reported deposit balances.

The analysis dataset includes:

- **75,859** office records
- **4,249** unique banking institutions
- Approximately **$19.05 trillion** in reported deposits

### Key Variables

| Variable | Description |
|---|---|
| `YEAR` | Reporting year |
| `CERT` | FDIC certificate number identifying an institution |
| `NAMEFULL` | Full name of the banking institution |
| `BRNUM` | Branch number |
| `UNINUMBR` | Unique office identifier |
| `STALPBR` | State abbreviation |
| `CITYBR` | City where the office is located |
| `DEPSUMBR` | Reported deposits, in thousands of U.S. dollars |
| `SIMS_LATITUDE` | Office latitude |
| `SIMS_LONGITUDE` | Office longitude |

**Note:** Deposit values are reported in thousands of U.S. dollars. To convert them into dollars, multiply by 1,000.

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab
- Streamlit *(planned for interactive dashboard deployment)*

## 🔍 Methodology

### 1. Data Validation and Preparation

- Inspected dataset dimensions and column names.
- Checked missing values and duplicate office identifiers.
- Verified deposit totals and the reporting period.
- Examined zero-deposit records and branch-number classifications.

### 2. Geographic Deposit Analysis

- Aggregated deposits by state.
- Compared total and median deposits across states.
- Identified states with the largest reported deposit volumes.
- Examined differences between total deposits and typical office-level balances.

### 3. Banking Institution Analysis

- Aggregated deposits by banking institution.
- Ranked institutions by total deposits.
- Calculated each institution's share of total deposits.
- Examined the geographic reach of selected institutions.

### 4. Market Concentration Analysis

The Herfindahl-Hirschman Index (HHI) was calculated using institution-level deposit market shares within each state.

\[
HHI = \sum_{i=1}^{N} s_i^2
\]

Where \(s_i\) is institution \(i\)'s deposit market share expressed as a percentage.

The analysis also calculates the **Top-3 Deposit Share**, which measures the combined percentage of state deposits held by the three largest institutions.

The HHI categories used in this project are descriptive screening thresholds:

- Below 1,500: Lower concentration
- 1,500–2,500: Moderate concentration
- Above 2,500: High concentration

These categories are used for exploratory analysis and should not be interpreted as a formal regulatory assessment.

### 5. Deposit Distribution and Outlier Analysis

- Compared deposit distributions for records with `BRNUM = 0` and `BRNUM != 0`.
- Used medians and interquartile ranges to understand typical deposit levels.
- Applied logarithmic scaling to visualize highly skewed distributions.
- Identified unusually large deposit records for further investigation.

## 📈 Key Findings

### 1. Geographic Differences in Deposit Volumes

New York recorded approximately **$2.77 trillion** in deposits, followed by California at approximately **$1.87 trillion** and Texas at approximately **$1.59 trillion**.

These results demonstrate substantial differences in the geographic distribution of reported deposits.

### 2. Differences in Deposit Concentration

The following results were obtained for five selected states:

| State | HHI | Top-3 Deposit Share |
|---|---:|---:|
| South Dakota | 4,674.31 | 96.16% |
| California | 1,196.68 | 56.38% |
| New York | 1,549.26 | 54.34% |
| Utah | 1,246.82 | 51.65% |
| Texas | 843.56 | 46.23% |

South Dakota exhibits the highest concentration among these five states, while Texas has the lowest HHI. These measures describe the distribution of deposits in the dataset, not necessarily competition in local retail banking markets.

### 3. Largest Banking Institutions

The three largest institutions by aggregate deposits were:

| Institution | Total Deposits | Share of Dataset |
|---|---:|---:|
| JPMorgan Chase Bank | $2.23 trillion | 11.69% |
| Bank of America | $1.98 trillion | 10.41% |
| Wells Fargo Bank | $1.55 trillion | 8.16% |

Together, these institutions accounted for approximately **30.26% of total reported deposits**.

### 4. Skewed Deposit Distributions

The distribution analysis revealed substantial differences between mean and median deposits, along with extremely large observations.

This supports the use of medians, distribution plots, and outlier investigation alongside aggregate deposit totals.

## 💡 Business Recommendations

Based on the findings, the following actions are recommended:

1. **Monitor deposit concentration:** Investigate states where a small number of institutions account for a large share of reported deposits.
2. **Use multiple market indicators:** Combine total deposits, institution-level shares, office counts, and concentration metrics when comparing geographic markets.
3. **Track major institutions:** Monitor changes in deposit shares and geographic distribution when comparable data from multiple years are available.
4. **Investigate extreme observations:** Verify unusually large deposit records before using them in branch-level comparisons.
5. **Improve performance measurement:** Incorporate operating costs, customer numbers, lending activity, transaction volumes, and profitability data to develop more complete measures of banking performance.

## ⚠️ Limitations

- The analysis covers a single reporting period and cannot establish deposit growth over time.
- Deposit volume alone does not measure profitability, operational efficiency, or customer satisfaction.
- The meaning of `BRNUM = 0` must be verified against the official FDIC data definitions before these records are classified as headquarters or excluded from branch comparisons.
- State-level concentration can be influenced by specialized institutions and the geographic locations of their reported offices.
- HHI thresholds are used as exploratory screening categories, not as a definitive assessment of market competition.
- Further validation is required before interpreting office-level deposits as a measure of branch productivity.

## 🚀 Project Deliverables

- Data validation and exploratory analysis
- Geographic deposit comparisons
- Institution-level deposit rankings
- HHI and Top-3 Deposit Share calculations
- Deposit distribution and outlier analysis
- Business findings and recommendations
- Interactive Streamlit dashboard *(planned)*

## 📂 Project Structure

```text
Banking-Branch-Performance-Analytics/
│
├── data/
│   └── README.md
│
├── notebooks/
│   └── banking_branch_performance_analysis.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

*The structure above is a suggested organization. Update filenames to match the files actually included in your repository. Do not commit restricted or sensitive data.*

## ▶️ How to Run the Project

1. Clone the repository.
2. Install the required Python libraries.
3. Place the permitted dataset in the appropriate directory.
4. Open the notebook in Jupyter Notebook or Google Colab.
5. Run the analysis cells in order.

Install the core libraries using:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

When the Streamlit dashboard is ready, install Streamlit and run:

```bash
pip install streamlit
streamlit run app.py
```

## 🏁 Conclusion

This project demonstrates how statistical analysis and business analytics can be applied to banking data to examine deposit distribution, compare geographic markets, identify concentration patterns, and investigate extreme observations.

It also highlights an essential analytical principle: **large deposit balances do not automatically imply superior banking performance**. Reliable business recommendations require appropriate metrics, careful interpretation, and additional operational and financial information.

## 👤 Author

**Leny Napala**

Business Analyst | Business Analytics | Data Analysis | Statistical Modeling

## 📄 Data Source

Federal Deposit Insurance Corporation (FDIC) — Summary of Deposits (SOD).

Official website: https://www.fdic.gov/

