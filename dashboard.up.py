import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sewanee Recycling Dashboard")

st.title("♻️ Sewanee Recycling Dashboard")
st.write("Tracking recycling performance across campus")

# Load recycling data automatically
df = pd.read_csv("recycling_data.csv")

# Calculate contamination rates
df["Contamination_Rate"] = (
    df["Contaminated_Weight"] / df["Total_Weight"] * 100
)

# Calculate campus totals
total_weight = df["Total_Weight"].sum()
contaminated_weight = df["Contaminated_Weight"].sum()
aluminum_weight = df["Aluminum_Weight"].sum()

st.subheader("Campus Recycling Statistics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Audited", f"{total_weight} lbs")
col2.metric(
    "Contamination Rate",
    f"{contaminated_weight / total_weight * 100:.1f}%"
)
col3.metric("Aluminum Collected", f"{aluminum_weight} lbs")

st.subheader("Contamination by Organization")

st.bar_chart(
    df.set_index("Organization")["Contamination_Rate"]
)

st.subheader("Organization Rankings")

rankings = df.sort_values("Contamination_Rate")
st.dataframe(rankings, hide_index=True)

st.subheader("Raw Recycling Data")
st.dataframe(df, hide_index=True)

st.caption("Demonstration data — not actual Sewanee measurements.")
