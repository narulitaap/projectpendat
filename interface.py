import streamlit as st
import re
import pandas as pd 
import numpy as np

st.title("""
form input data, by Arin Comel
""")

#Fractional Knapsack Problem
#Getting input from user
kehamilan=int(st.number_input("Berapa Kali Hamil: ",0))
glukosa=int(st.number_input("Berapa Konsentrasi Glukosa Plasma : ",0))
tekanandarah=int(st.number_input("Berapa Tekanan darah diastolik : ",0))
ketebalankulit=int(st.number_input("Berapa Ketebalan lipatan kulit trisep : ",0))
insulin=int(st.number_input(" Berapa Insulin serum: ",0))
bmi=int(st.number_input(" Indeks massa tubuh : ",0))
age=int(st.number_input(" Masukkan Usia : ",0))
submit = st.button("submit")


if submit:
    st.info("Jadi,dinyakataan . ")


