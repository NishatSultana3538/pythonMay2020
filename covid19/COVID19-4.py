# cases : country/region - province/state wise
# Recovered, Deaths, Confirmed
import pandas as pd
covid_data= pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/05-13-2020.csv")

data = covid_data.groupby(['Country_Region', 'Province_State'])['Recovered' , 'Deaths', 'Confirmed'] .max()
pd.set_option('display.max_rows' , None)
