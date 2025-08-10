import requests

url = "https://www.stats.govt.nz/assets/Uploads/Effects-of-COVID-19-on-trade/Effects-of-COVID-19-on-trade-At-15-December-2021-provisional/Download-data/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"
filename = "covid_trade_data.csv"

response = requests.get(url)

with open(filename, "wb") as f:
    f.write(response.content)

print(f"CSV file downloaded and saved as {filename}")
