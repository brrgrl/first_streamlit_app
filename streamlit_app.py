# This is a new file for the Streamlit App

import streamlit
import pandas

streamlit.title("My Mom's New Healthy Diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruit_list_url = 'https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt'
my_fruit_list = pandas.read_csv(fruit_list_url)
streamlit.dataframe(my_fruit_list)

