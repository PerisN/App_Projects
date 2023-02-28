import streamlit as st
import pandas as pd
import plotly.express as px

# Load earthquake data
earthquake_df = pd.read_csv("Data.csv")

# Define page configurations
st.set_page_config(page_title="Earthquake Exploration App", page_icon=":earth_americas:", layout="wide")
st.markdown("<h1 style='text-align: center; color: #d64848;'>Earthquake Exploration App</h1>", unsafe_allow_html=True)

# Create a separate page for data exploration
def data_exploration():
    st.title("Data Exploration")

    # Display basic statistics
    st.header("Basic Statistics")
    st.write(earthquake_df.describe())

    # Display missing data
    st.header("Missing Data")
    st.write(earthquake_df.isna().sum())

    # Display correlation matrix
    st.header("Correlation Matrix")
    st.write(earthquake_df.corr())

    # Display histogram of magnitudes
    st.header("Distribution of Magnitudes")
    fig = px.histogram(earthquake_df, x="Magnitude", nbins=20)
    fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white')
    fig.update_traces(marker_color='#d64848')
    st.plotly_chart(fig)

# Create the main page
def main():
    # Add a menu to switch between pages
    menu = ["Home", "Data Exploration"]
    choice = st.sidebar.selectbox("Select a page", menu)

    # Display the selected page
    if choice == "Home":
        st.sidebar.subheader("Magnitude Range")

        # Add slider for magnitude range
        mag_min, mag_max = st.sidebar.slider("Select a range of magnitudes", 5.0, 10.0, (5.0, 10.0), 0.1)

        # Filter data by magnitude range
        filtered_data = earthquake_df[(earthquake_df["Magnitude"] >= mag_min) & (earthquake_df["Magnitude"] <= mag_max)]

        # Display map of earthquakes
        st.header("Map of Earthquakes")
        fig = px.scatter_geo(filtered_data, lat="Latitude", lon="Longitude", color="Magnitude",
                             color_continuous_scale="reds", projection="natural earth", 
                             hover_data=["Magnitude"])
        fig.update_layout(autosize=True, margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig)

    elif choice == "Data Exploration":
        data_exploration()

if __name__ == "__main__":
    main()