import pandas as pd
import matplotlib.pyplot as plt

url = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"

wdi_data = pd.read_csv(url)


columns = [
    "Mortality rate, infant (per 1,000 live births)",
    "GDP per capita (constant 2010 US$)",
    "Country Name",
]

df = wdi_data[columns]

plt.scatter(
    df["Mortality rate, infant (per 1,000 live births)"],
    df["GDP per capita (constant 2010 US$)"],
)
