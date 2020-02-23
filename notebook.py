
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Input data

low_world_production = np.array([
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

low_row_production = np.array([
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

low_price =  np.array([
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

high_world_production = np.array([
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

high_row_production = np.array([
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

high_price = np.array([
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

# Fit ROW Supply Curve

row_production = np.hstack((low_row_production, high_row_production))
row_price      = np.hstack((low_price, high_price))

p_row = np.polyfit(row_production, row_price, 1)

plt.plot(low_row_production, low_price, "*")
plt.plot(high_row_production, high_price, "*")
plt.plot(row_production, p_row[0] * row_production + p_row[1], 
         label=f"Price = {p_row[0]:.5f} * Production + {p_row[1]:.2f}")
plt.legend()
plt.title("ROW Supply Curve")
st.pyplot()

#  # OPEC Price vs Production
#  plt.plot(low_world_production - low_row_production, low_price, "*")
#  plt.plot(high_world_production - high_row_production, high_price, "*")
#  plt.title("OPEC Price vs Production")
#  st.pyplot()

# World low demand curve
p_low = np.polyfit(low_world_production, low_price, 1)

plt.plot(low_world_production, low_price, "*")
plt.plot(low_world_production, p_low[0]*low_world_production + p_low[1],
         label=f"Price = {p_low[0]:.5f} * Production + {p_low[1]:.2f}")
plt.title("World Low Demand Curve")
plt.legend()
st.pyplot()

# World high demand curve
p_high = np.polyfit(high_world_production, high_price, 1)

plt.plot(high_world_production, high_price, "*")
plt.plot(high_world_production, p_high[0]*high_world_production + p_high[1],
         label=f"Price = {p_high[0]:.5f} * Production + {p_high[1]:.2f}")
plt.title("World High Demand Curve")
plt.legend()
st.pyplot()

### Simulated Demand Curves

opec_supply = 15000
f"## OPEC Supply: {opec_supply}"

p_demand = p_low

production_values = np.linspace(40000, 85000)

price = 1/(1 - p_demand[0] / p_row[0]) * (-p_demand[0]*p_row[1]/p_row[0] + p_demand[0]*opec_supply + p_demand[1])
f"## Barrel Price: {price:0.2f}"

plt.plot(production_values, p_row[0]*production_values + p_row[1], label="ROW Supply")
plt.plot(production_values, p_demand[0]*production_values + p_demand[1], label="World Demand")
plt.plot(production_values, p_row[0]*(production_values - opec_supply) + p_row[1], label="ROW + OPEC Supply")
plt.plot(production_values, [price]*len(production_values), label="Price")
plt.ylim(0, 250)
plt.legend()
plt.title("Supply Demand Sim")
st.pyplot()

# Compute contries marginal costs
class Country:
    def __init__(self, name, total_reserves, production_capacity, marginal_cost):
        self._name = name
        self._production_capacity = production_capacity
        self._marginal_cost = marginal_cost

countries = {
    "Saudi Arabia" : Country("Saudi Arabia", 108000, 12000, 9),
    "Iran" : Country("Iran", 41400, 4600, 10),
    "Iraq" : Country("Iraq", 333000, 3700, 16),
    "Kuwait" : Country("Kuwait", 29700, 3300, 13),
    "UAE" : Country("UAE", 27000, 3000, 5),
    "Venezuela" : Country("Venezula", 39600, 4400, 20),
    "Nigeria" : Country("Nigeria", 24300, 2700, 7),
}

FINAL_PRICE = 70
INTEREST_RATE = 0.05
FINAL_PERIOD = 10

def barrel_value(day, country):
    final_sale_value = FINAL_PRICE - country._marginal_cost
    present_value = final_sale_value / (1 + INTEREST_RATE)**(FINAL_PERIOD - day)
    return present_value


def plot_barrel_value(country):
    periods = [i+1 for i in range(FINAL_PERIOD)]
    barrel_values = [barrel_value(day, countries[country]) for day in periods]

    plt.plot(periods, barrel_values, "*")
    plt.title(f"{country} Barrel Minimum Value")
    plt.xlabel("Day")
    plt.ylabel("Present Value")
    st.pyplot()

plot_barrel_value("Saudi Arabia")

OPEC_MAX_PRODUCTION = sum([countries[name]._production_capacity for name in countries])
f"### OPEC Max Production: {OPEC_MAX_PRODUCTION}"

def countries_min_price(day):
    country_names = list(countries.keys())
    marginal_costs = [barrel_value(day, countries[name]) + countries[name]._marginal_cost for name in countries]
    y_pos = np.arange(len(country_names))
    plt.bar(y_pos, marginal_costs, label=f"Day {day}")
    plt.xticks(y_pos, country_names)
    plt.ylim(40, 80)
    plt.title(f"Country Minmum Price")

countries_min_price(10)
countries_min_price(1)
plt.legend()
st.pyplot()

