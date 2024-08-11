import altair as alt
import pandas as pd
import numpy as np
import streamlit as st

# Function to search for movie or TV show titles with season and episode
def search_titles(data, query):
    results = data[data['title'].str.contains(query, case=False, na=False)]
    return results

# Function to search subtitles with AI transcripts
def search_subtitles(data, query):
    results = data[data['transcript'].str.contains(query, case=False, na=False)]
    return results

# Load data
@st.cache
def load_data():
    # Replace with the path to your data file
    data = pd.read_csv('path_to_your_data_file.csv')
    return data

data = load_data()

# Streamlit app
st.title('Movie and TV Show Search')

# Search for titles
st.header('Search for Movie or TV Show Titles')
title_query = st.text_input('Enter title to search for:')
if title_query:
    title_results = search_titles(data, title_query)
    st.write('Results:')
    st.write(title_results)

# Search for subtitles
st.header('Search Subtitles with AI Transcripts')
subtitle_query = st.text_input('Enter subtitle to search for:')
if subtitle_query:
    subtitle_results = search_subtitles(data, subtitle_query)
    st.write('Results:')
    st.write(subtitle_results)
