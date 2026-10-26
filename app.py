
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# --------------------------------------------------
# 1. Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Banking Branch Performance Analytics",
    page_icon="🏦",
    layout="wide"
)

# --------------------------------------------------
# 2. Dashboard title
# --------------------------------------------------
st.title("🏦 Banking Branch Performance Analytics")
st.caption(
    "FDIC Summary of Deposits | Deposit Distribution, "
    "Institution Rankings and Market Concentration"
)

# --------------------------------------------------
# 3. Load the dataset
# --------------------------------------------------
DATA_FILE = Path("SOD_CustomDownload_2026_06_30 (1).csv")

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path, low_memory=False)

    # Convert numeric fields safely
    for col in ["DEPSUMBR", "CERT", "BRNUM", "UNINUMBR", "YEAR"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

if not DATA_FILE.exists():
    st.error(
        f"Dataset not found: {DATA_FILE.name}. "
        "Check the filename and its location in your GitHub repository."
    )
    st.stop()

df = load_data(str(DATA_FILE))

# --------------------------------------------------
# 4. Validate essential columns
# --------------------------------------------------
required_columns = [
    "CERT", "NAMEFULL", "STALPBR", "DEPSUMBR", "UNINUMBR"
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    st.error(f"Missing required columns: {missing_columns}")
    st.stop()

# Deposits are reported in thousands of dollars.
# Divide by 1,000,000 to express deposits in billions.
df["DEPOSITS_BILLION"] = df["DEPSUMBR"] / 1_000_000

# --------------------------------------------------
# 5. Sidebar filters
# --------------------------------------------------
st.sidebar.header("Dashboard Filters")

states = sorted(df["STALPBR"].dropna().unique().tolist())

selected_states = st.sidebar.multiselect(
    "Select states",
    options=states,
    default=states
)

filtered_df = df[df["STALPBR"].isin(selected_states)].copy()

# --------------------------------------------------
# 6. Key performance indicators
# --------------------------------------------------
total_deposits = filtered_df["DEPSUMBR"].sum() / 1_000_000
institution_count = filtered_df["CERT"].nunique()
office_count = filtered_df["UNINUMBR"].nunique()
state_count = filtered_df["STALPBR"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Deposits", f"${total_deposits:,.2f}B")
col2.metric("Institutions", f"{institution_count:,}")
col3.metric("Office Records", f"{office_count:,}")
col4.metric("States", f"{state_count:,}")

st.divider()

# --------------------------------------------------
# 7. Deposit distribution by state
# --------------------------------------------------
st.subheader("📍 Deposit Distribution by State")

state_analysis = (
    filtered_df.groupby("STALPBR", as_index=False)
    .agg(
        Total_Deposits=("DEPSUMBR", "sum"),
        Office_Records=("UNINUMBR", "nunique"),
        Institutions=("CERT", "nunique")
    )
)

state_analysis["Deposits_Billion"] = (
    state_analysis["Total_Deposits"] / 1_000_000
)

state_analysis = state_analysis.sort_values(
    "Deposits_Billion", ascending=False
)

fig_state = px.bar(
    state_analysis.head(15),
    x="STALPBR",
    y="Deposits_Billion",
    color="Deposits_Billion",
    color_continuous_scale="Viridis",
    title="Top 15 States by Total Deposits",
    labels={
        "STALPBR": "State",
        "Deposits_Billion": "Deposits (USD billions)"
    }
)

st.plotly_chart(fig_state, use_container_width=True)

# --------------------------------------------------
# 8. Top banking institutions
# --------------------------------------------------
st.subheader("🏦 Top 10 Institutions by Deposits")

institution_analysis = (
    filtered_df.groupby(["CERT", "NAMEFULL"], as_index=False)
    .agg(Total_Deposits=("DEPSUMBR", "sum"))
)

institution_analysis["Deposits_Billion"] = (
    institution_analysis["Total_Deposits"] / 1_000_000
)

institution_analysis = institution_analysis.sort_values(
    "Deposits_Billion", ascending=False
).head(10)

fig_institutions = px.bar(
    institution_analysis.sort_values(
        "Deposits_Billion", ascending=True
    ),
    x="Deposits_Billion",
    y="NAMEFULL",
    color="Deposits_Billion",
    color_continuous_scale="Plasma",
    orientation="h",
    title="Top 10 Institutions by Total Deposits",
    labels={
        "NAMEFULL": "Institution",
        "Deposits_Billion": "Deposits (USD billions)"
    }
)

st.plotly_chart(fig_institutions, use_container_width=True)

# --------------------------------------------------
# 9. Data preview
# --------------------------------------------------
with st.expander("🔎 Explore the dataset"):
    st.write(f"Rows: {len(filtered_df):,}")
    st.dataframe(filtered_df.head(100), use_container_width=True)

st.caption(
    "Educational business analytics project. "
    "Deposit size alone does not measure profitability or efficiency."
)

