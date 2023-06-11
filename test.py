import requests

def fetch_indicator_data(country_code, indicator_code):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json"
    response = requests.get(url)
    data = response.json()
    
    indicator_data = {}
    for item in data[1]:
        year = item['date']
        value = item['value']
        indicator_data[year] = value

    return indicator_data

countries = ["USA", "GBR", "FRA"]
indicators = ["SP.POP.TOTL", "NY.GDP.MKTP.CD"]

for country in countries:
    for indicator in indicators:
        data = fetch_indicator_data(country, indicator)
        print(f"{country} - {indicator}:\n{data}\n")
