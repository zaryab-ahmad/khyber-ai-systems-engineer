import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Regional Analytics", layout="wide")

st.title("🚀 Regional Analytics Dashboard")

# 2. Sidebar for Navigation/Inputs
st.sidebar.header("Configuration")
region = st.sidebar.selectbox(
    'Select the Target Region',
    ('Peshawar', 'Mardan', 'Swat', 'Kohat')
)

# 3. Main Interface Widgets
threshold = st.slider('Select Success Threshold (%)', 0, 100, 50)

# Dynamic Filtering Text
st.write(f"Displaying results for **{region}** with a threshold of **{threshold}%**")

# 4. Analysis Logic Trigger
if st.button('Run Analysis'):
    st.success(f"Analysis complete for {region}!")
    
    # Generate positive random data for the analysis
    df = pd.DataFrame({
        'Crop Yield': np.random.uniform(50, 100, 20),
        'Rainfall': np.random.uniform(10, 50, 20),
        'Temperature': np.random.uniform(15, 45, 20)
    })

    st.write("### Analysis Data Preview", df)

    # 5. Interactive Visualization
    # Using 'Temperature' for size (ensured positive to avoid ValueErrors)
    fig = px.scatter(
        df, 
        x="Rainfall", 
        y="Crop Yield", 
        size="Temperature", 
        color="Crop Yield",
        title=f"Impact of Rainfall on Crop Yield in {region}",
        template="plotly_dark",
        labels={"Crop Yield": "Yield (Tons)", "Rainfall": "Rainfall (mm)"}
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Click 'Run Analysis' to generate the regional report and visualization.")
