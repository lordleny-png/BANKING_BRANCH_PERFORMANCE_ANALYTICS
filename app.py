
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
# 9. Market concentration analysis
# --------------------------------------------------
st.divider()
st.subheader("📊 Market Concentration Analysis")

st.write(
    "The Herfindahl–Hirschman Index (HHI) measures how "
    "concentrated deposits are among banking institutions "
    "within each state. The Top-3 Share shows the percentage "
    "of deposits held by the three largest institutions."
)

# Aggregate deposits by state and institution
state_institution = (
    filtered_df.groupby(["STALPBR", "CERT"], as_index=False)
    .agg(Deposits=("DEPSUMBR", "sum"))
)

# Exclude institutions with no positive deposits
state_institution = state_institution[
    state_institution["Deposits"] > 0
].copy()

# Calculate each institution's share within its state
state_institution["State_Total"] = (
    state_institution.groupby("STALPBR")["Deposits"]
    .transform("sum")
)

state_institution["Share_Percent"] = (
    state_institution["Deposits"]
    / state_institution["State_Total"] * 100
)

# HHI = sum of squared percentage shares
state_institution["Share_Squared"] = (
    state_institution["Share_Percent"] ** 2
)

hhi_by_state = (
    state_institution.groupby("STALPBR", as_index=False)
    .agg(HHI=("Share_Squared", "sum"))
)

# Calculate the top-three deposit share in each state
top3_by_state = (
    state_institution.sort_values(
        ["STALPBR", "Deposits"],
        ascending=[True, False]
    )
    .groupby("STALPBR")
    .head(3)
    .groupby("STALPBR", as_index=False)
    .agg(Top3_Deposits=("Deposits", "sum"))
)

state_totals = (
    state_institution.groupby("STALPBR", as_index=False)
    .agg(Total_Deposits=("Deposits", "sum"))
)

concentration = (
    state_totals
    .merge(hhi_by_state, on="STALPBR")
    .merge(top3_by_state, on="STALPBR")
)

concentration["Top3_Share_Percent"] = (
    concentration["Top3_Deposits"]
    / concentration["Total_Deposits"] * 100
)

# Descriptive screening categories, not legal conclusions
concentration["HHI_Category"] = pd.cut(
    concentration["HHI"],
    bins=[-float("inf"), 1500, 2500, float("inf")],
    labels=["Lower", "Moderate", "High"],
    right=False
)

# Show the most concentrated states
top_concentrated = concentration.sort_values(
    "HHI", ascending=False
).head(15)

fig_hhi = px.bar(
    top_concentrated.sort_values("HHI"),
    x="HHI",
    y="STALPBR",
    color="HHI_Category",
    color_discrete_map={
        "Lower": "#2E86AB",
        "Moderate": "#F6AE2D",
        "High": "#D1495B"
    },
    orientation="h",
    title="15 States with the Highest Deposit Concentration",
    labels={
        "STALPBR": "State",
        "HHI": "Herfindahl–Hirschman Index",
        "HHI_Category": "Screening category"
    }
)

st.plotly_chart(fig_hhi, use_container_width=True)

# Compare top-three shares
top3_chart = concentration.sort_values(
    "Top3_Share_Percent", ascending=False
).head(15)

fig_top3 = px.bar(
    top3_chart.sort_values("Top3_Share_Percent"),
    x="Top3_Share_Percent",
    y="STALPBR",
    color="Top3_Share_Percent",
    color_continuous_scale="Viridis",
    orientation="h",
    title="Top-3 Institutions' Share of State Deposits",
    labels={
        "STALPBR": "State",
        "Top3_Share_Percent": "Top-3 deposit share (%)"
    }
)

st.plotly_chart(fig_top3, use_container_width=True)

# Allow users to inspect exact results
with st.expander("View market concentration results"):
    display_concentration = concentration[
        [
            "STALPBR",
            "Total_Deposits",
            "HHI",
            "HHI_Category",
            "Top3_Share_Percent"
        ]
    ].sort_values("HHI", ascending=False)

    st.dataframe(
        display_concentration.round(2),
        use_container_width=True
    )

st.caption(
    "HHI categories are descriptive screening bands. "
    "State-level concentration does not necessarily measure "
    "competition in a local banking market."
)

# --------------------------------------------------
# 10. Deposit distribution and data quality
# --------------------------------------------------
st.divider()
st.subheader("🔎 Deposit Distribution & Data Quality")

st.write(
    "Analyze the distribution of deposits across office records, "
    "compare BRNUM groups, and identify unusual values requiring "
    "further investigation."
)

# Create a working dataset
distribution_df = filtered_df.copy()

distribution_df["BRNUM_Group"] = distribution_df["BRNUM"].apply(
    lambda x: "BRNUM = 0" if x == 0
    else ("BRNUM != 0" if pd.notna(x) else "Unknown")
)

# Deposit amounts in millions of USD
distribution_df["Deposits_Million"] = (
    distribution_df["DEPSUMBR"] / 1000
)

# Summary indicators
zero_deposits = (
    distribution_df["DEPSUMBR"].fillna(0).eq(0).sum()
)

missing_deposits = distribution_df["DEPSUMBR"].isna().sum()

positive_deposits = distribution_df[
    distribution_df["DEPSUMBR"] > 0
].copy()

kpi1, kpi2, kpi3 = st.columns(3)

kpi1.metric("Zero-Deposit Records", f"{zero_deposits:,}")
kpi2.metric("Missing Deposit Values", f"{missing_deposits:,}")
kpi3.metric("Positive-Deposit Records", f"{len(positive_deposits):,}")

# Compare deposit distributions
st.markdown("### Deposit Distribution by BRNUM Group")

box_data = positive_deposits[
    positive_deposits["BRNUM_Group"] != "Unknown"
].copy()

if not box_data.empty:
    fig_box = px.box(
        box_data,
        x="BRNUM_Group",
        y="Deposits_Million",
        color="BRNUM_Group",
        color_discrete_map={
            "BRNUM = 0": "#2E86AB",
            "BRNUM != 0": "#F6AE2D"
        },
        log_y=True,
        points=False,
        title="Deposit Distribution by BRNUM Group (Log Scale)",
        labels={
            "BRNUM_Group": "BRNUM group",
            "Deposits_Million": "Deposits (USD millions)"
        }
    )

    st.plotly_chart(fig_box, use_container_width=True)

    st.caption(
        "The logarithmic scale makes it easier to compare typical "
        "deposit values when a few records are extremely large. "
        "Zero deposits are excluded from this plot because log scales "
        "cannot display zero."
    )

# Calculate group-level statistics
st.markdown("### Group-Level Statistics")

group_stats = (
    distribution_df.groupby("BRNUM_Group", as_index=False)
    .agg(
        Record_Count=("UNINUMBR", "nunique"),
        Median_Deposits=("DEPSUMBR", "median"),
        Mean_Deposits=("DEPSUMBR", "mean"),
        Zero_Deposit_Records=(
            "DEPSUMBR",
            lambda x: (x.fillna(0) == 0).sum()
        )
    )
)

# Convert deposit statistics from thousands to millions
group_stats["Median_Deposits"] /= 1000
group_stats["Mean_Deposits"] /= 1000

group_stats = group_stats.rename(
    columns={
        "Median_Deposits": "Median (USD millions)",
        "Mean_Deposits": "Mean (USD millions)"
    }
)

st.dataframe(
    group_stats.round(2),
    use_container_width=True,
    hide_index=True
)

# Investigate unusually large records
st.markdown("### Largest Individual Office Records")

top_records = (
    distribution_df.sort_values("DEPSUMBR", ascending=False)
    .head(10)
    .copy()
)

top_records["Deposits (USD billions)"] = (
    top_records["DEPSUMBR"] / 1_000_000
)

display_columns = [
    "NAMEFULL",
    "STALPBR",
    "CITYBR",
    "BRNUM",
    "Deposits (USD billions)"
]

available_columns = [
    col for col in display_columns if col in top_records.columns
]

st.dataframe(
    top_records[available_columns].round(3),
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Large deposit records are not automatically errors. "
    "Verify their meaning and reporting context before excluding them."
)



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

