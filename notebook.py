
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

odd_world_production = np.array([
    61440,
    62083,
    62769,
    64494,
    66023,
    67769,
    69652,
    70206,
    73530,
    74540,
    76258,
    75502
])

odd_row_production = np.array([
    46919,
    46956,
    46902,
    46093,
    46054,
    45296,
    45284,
    44516,
    44020,
    43774,
    43754,
    43157
])

odd_price =  np.array([
    145.43,
    145.21,
    134.41,
    121.29,
    114.24,
    107.88,
    103.73,
    94.62,
    86.70,
    75.07,
    73.26,
    67.35
])

even_world_production = np.array([
    62779,
    63802,
    63776,
    66776,
    68713,
    71217,
    69821,
    73285,
    76214,
    78604,
    77546,
    79611
])

even_row_production = np.array([
    47828,
    47730,
    47964,
    47365,
    46720,
    46283,
    45829,
    45151,
    44819,
    44783,
    44511,
    44173
])

even_price = np.array([
    158.68,
    159.49,
    157.13,
    140.48,
    135.59,
    125.93,
    121.31,
    102.97,
    100.41,
    96.37,
    88.96,
    86.35
])

plt.plot(odd_row_production, odd_price, "*")
plt.plot(even_row_production, even_price, "*")
plt.title("ROW Price vs Production")
st.pyplot()

plt.plot(odd_world_production - odd_row_production, odd_price, "*")
plt.plot(even_world_production - even_row_production, even_price, "*")
plt.title("OPEC Price vs Production")
st.pyplot()

plt.plot(world_production, odd_price, "*")
plt.plot(even_world_production - even_row_production, even_price, "*")
plt.title("OPEC Price vs Production")
st.pyplot()

#  class Country:
    #  def __init__(self, name, V

#  def barrel_value(day,
