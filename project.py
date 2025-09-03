import streamlit as st
import pandas as pd
import plotly.express as px

#PAGE CONFIG 
st.set_page_config(page_title="Menu-Driven Dashboard", layout="wide")

# MENU OPTIONS 
menu = ["Home", "Data Upload & Preview", "Data Visualization", "Summary Statistics", "About"]
choice = st.sidebar.selectbox("Select a Page", menu)

#  SESSION STATE TO STORE DATA 
if 'df' not in st.session_state:
    st.session_state.df = None

#  HOME PAGE 
if choice == "Home":
    st.title("📊 Smart Data Visualization Hub")
    st.markdown("""
    Welcome to the **Dashbosard** built with **Streamlit**.
    
    **Features:**
    - Upload and preview CSV datasets
    - Generate interactive visualizations
    - View summary statistics
    - Explore data easily via a sidebar menu
    """)

#  DATA UPLOAD PAGE 
elif choice == "Data Upload & Preview":
    st.title("📂 Data Upload & Preview")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        st.session_state.df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")
        st.subheader("🔹 Data Preview")
        st.dataframe(st.session_state.df.head())
        st.write(f"**Shape:** {st.session_state.df.shape[0]} rows × {st.session_state.df.shape[1]} columns")

# DATA VISUALIZATION PAGE 
elif choice == "Data Visualization":
    st.title("📈 Data Visualization")
    
    if st.session_state.df is not None:
        df = st.session_state.df
        st.subheader("Select Columns for Visualization")
        
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        all_cols = df.columns.tolist()
        
        x_axis = st.selectbox("Select X-axis", all_cols)
        y_axis = st.selectbox("Select Y-axis", numeric_cols)
        chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot"])
        
        if st.button("Generate Chart"):
            if chart_type == "Line Chart":
                fig = px.line(df, x=x_axis, y=y_axis, title=f"{chart_type} of {y_axis} vs {x_axis}")
            elif chart_type == "Bar Chart":
                fig = px.bar(df, x=x_axis, y=y_axis, title=f"{chart_type} of {y_axis} vs {x_axis}")
            elif chart_type == "Scatter Plot":
                fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{chart_type} of {y_axis} vs {x_axis}")
            
            
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠ Please upload a dataset first!")

#  SUMMARY STATISTICS PAGE 
elif choice == "Summary Statistics":
    st.title("📊 Summary Statistics")
    
    if st.session_state.df is not None:
        df = st.session_state.df
        st.subheader("🔹 Basic Statistics")
        st.dataframe(df.describe())
        
        st.subheader("🔹 Missing Values")
        st.dataframe(df.isnull().sum())
        
        st.subheader("🔹 Data Types")
        st.dataframe(pd.DataFrame(df.dtypes, columns=["Data Type"]))
    else:
        st.warning("⚠ Please upload a dataset first!")

# ABOUT PAGE 
elif choice == "About":
    st.title("About This Dashboard")
    st.markdown("""
    **Developed with:** Streamlit, Pandas, Plotly  
    **Features:** Data upload, visualization, and statistics    
    
    This is a **menu-driven Python project** using Streamlit, perfect for learning **interactive dashboards**.
    """)
