import streamlit as st
import pandas as pd

st.title("Sewanee Recycling Dashboard")
st.write("Tracking recycling and contamination across campus")

uploaded_file = st.file_uploader(
    "Upload recycling data",
    type="csv"
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    df["Contamination_Rate"] = (
        df["Contaminated_Weight"] / df["Total_Weight"] * 100
    )

    total_weight = df["Total_Weight"].sum()
    total_contamination = df["Contaminated_Weight"].sum()
    total_aluminum = df["Aluminum_Weight"].sum()

    st.subheader("Campus Recycling Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Recycled", f"{total_weight} lbs")
    col2.metric(
        "Contamination Rate",
        f"{total_contamination / total_weight * 100:.1f}%"
    )
    col3.metric("Aluminum Collected", f"{total_aluminum} lbs")

    st.subheader("Contamination by Organization")

    st.bar_chart(
        df.set_index("Organization")["Contamination_Rate"]
    )

    st.subheader("Organization Rankings")

    rankings = df.sort_values("Contamination_Rate")

    st.dataframe(rankings)

    st.subheader("Raw Recycling Data")
    st.dataframe(df)
