import pandas as pd
covid_data= pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-13-2020.csv")

print(covid_data)


print("\nDataset information:")

print(covid_data.info())
print("\nMissing data information:")
print(covid_data.isna().sum())