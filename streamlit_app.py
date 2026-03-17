import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Universal Data Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Universal Data Analytics Dashboard")

st.sidebar.header("Upload Dataset")

# Upload CSV
file = st.sidebar.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if file:

    df = pd.read_csv(file)

    st.success("Dataset Loaded Successfully ✅")

    # Show dataset
    if st.checkbox("Show Raw Data"):
        st.dataframe(df)

    # Detect columns
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    all_cols = df.columns.tolist()

    if len(numeric_cols) == 0:
        st.error("Dataset must contain numeric columns for plotting.")
        st.stop()

    # Sidebar settings
    st.sidebar.header("Visualization Settings")

    chart_type = st.sidebar.selectbox(
        "Select Chart Type",
        [
            "Line Chart",
            "Bar Chart",
            "Scatter Plot",
            "Histogram",
            "Box Plot",
            "Violin Plot",
            "Pie Chart",
            "Area Chart",
            "Correlation Heatmap",
            "3D Scatter Plot"
        ]
    )

    x_axis = st.sidebar.selectbox("Select X-axis", all_cols)
    y_axis = st.sidebar.selectbox("Select Y-axis", numeric_cols)

    st.subheader(f"{chart_type}")

    # Charts
    if chart_type == "Line Chart":
        fig = px.line(df, x=x_axis, y=y_axis)

    elif chart_type == "Bar Chart":
        fig = px.bar(df, x=x_axis, y=y_axis)

    elif chart_type == "Scatter Plot":
        fig = px.scatter(df, x=x_axis, y=y_axis)

    elif chart_type == "Histogram":
        fig = px.histogram(df, x=y_axis)

    elif chart_type == "Box Plot":
        fig = px.box(df, x=x_axis, y=y_axis)

    elif chart_type == "Violin Plot":
        fig = px.violin(df, x=x_axis, y=y_axis)

    elif chart_type == "Pie Chart":
        fig = px.pie(df, names=x_axis)

    elif chart_type == "Area Chart":
        fig = px.area(df, x=x_axis, y=y_axis)

    elif chart_type == "Correlation Heatmap":

        corr = df[numeric_cols].corr()

        fig = px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale="Blues"
        )

    elif chart_type == "3D Scatter Plot":

        z_axis = st.sidebar.selectbox("Select Z-axis", numeric_cols)

        fig = px.scatter_3d(
            df,
            x=x_axis,
            y=y_axis,
            z=z_axis
        )

    st.plotly_chart(fig, width="stretch")

    # KPIs
    st.subheader("📌 Dataset Insights")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Rows", len(df))
    col2.metric("Total Columns", len(df.columns))
    col3.metric("Average Value", round(df[y_axis].mean(), 2))

    # Top records
    st.subheader("🏆 Top Records")

    top_records = df.sort_values(y_axis, ascending=False).head(10)

    st.dataframe(top_records)

    # Download data
    st.download_button(
        label="📥 Download Dataset",
        data=df.to_csv(index=False),
        file_name="dataset.csv",
        mime="text/csv"
    )

else:

    st.info("Upload a CSV file to begin data analysis.")