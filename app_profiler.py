import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd

# Page title
st.title("Public Health & Environmental Research Profile")

# Core profile info
name = "Tshepo Ntlemeza"
field = "Public Health and Environmental Health"
institution = "Sefako Makgatho Health Sciences University"

# Intro section
st.header("Profile Overview")
st.write(
    """
    I am a public health–focused environmental biology graduate with a strong interest in
    disease prevention, community health systems, and sustainable health interventions.
    My work sits at the intersection of science, leadership, and service.
    """
)

st.write(f"**Name:** {name}")
st.write(f"**Field:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Health, environment, and people are deeply connected."
)

# Leadership & involvement
st.header("Leadership & Engagement")
st.write(
    """
    Alongside my academic training, I am actively involved in student leadership and
    community initiatives, including health advocacy, environmental action, and peer education.
    These roles have shaped how I approach research: practical, people-centred, and accountable.
    """
)

# Publications / outputs
st.header("Research Outputs & Publications")
uploaded_file = st.file_uploader(
    "Upload a CSV file of publications or academic outputs",
    type="csv"
)

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    keyword = st.text_input("Search by keyword (topic, year, or author)")
    if keyword:
        filtered = publications[
            publications.apply(
                lambda row: keyword.lower() in row.astype(str).str.lower().values,
                axis=1
            )
        ]
        st.write(f"Results matching '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all entries.")

# Trends section
st.header("Publication Trends")
if uploaded_file and "Year" in publications.columns:
    year_counts = publications["Year"].value_counts().sort_index()
    st.bar_chart(year_counts)
elif uploaded_file:
    st.write("No 'Year' column found to display trends.")

# Interests section
st.header("Current Interests")
st.write(
    """
    - Environmental determinants of health  
    - Preventive public health strategies  
    - Community-based health education  
    - Climate and health systems  
    - Student-led health advocacy
    """
)

# Contact section
st.header("Contact")
email = "tshepothabiso97@gmail.com"
phone = "071 063 8729"

st.write(f"**Email:** {email}")
st.write(f"**Phone:** {phone}")
