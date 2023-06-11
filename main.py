import requests

def fetch_indicator_data(country_id, indicator_code):
    url = f"https://api.worldbank.org/v2/country/{country_id}/indicator/{indicator_code}?format=json"
    response = requests.get(url)
    data = response.json()

    indicator_data = {}
    for item in data[1]:
        year = item['date']
        value = item['value']
        indicator_data[year] = value

    return indicator_data

def get_country_data():
    url = "https://api.worldbank.org/v2/country"
    params = {
        "format": "json",
        "per_page": 100,
        "fields": "id,name,region,adminregion,incomeLevel,lendingType,capitalCity,longitude,latitude",
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        for country in data[1]:
            country_id = country["id"]
            country_name = country["name"]

            print("Country ID:", country_id)
            print("Country Name:", country_name)
            print("Region:", country["region"]["value"])
            print("Admin Region:", country.get("adminregion", {}).get("value", None))
            print("Income Level:", country["incomeLevel"]["value"])
            print("Lending Type:", country["lendingType"]["value"])
            print("Capital City:", country["capitalCity"])
            print("Longitude:", country["longitude"])
            print("Latitude:", country["latitude"])
            print("============================")

            # Запрос данных о населении и ВВП для каждой страны
            parameters = [
                {"indicator": "SP.POP.TOTL", "parameter": "Population"},
                {"indicator": "NY.GDP.MKTP.CD", "parameter": "GDP"},
                {"indicator": "SL.UEM.TOTL.ZS", "parameter": "Unemployment rate"},
                {"indicator": "FP.CPI.TOTL.ZG", "parameter": "Inflation"},
                {"indicator": "NE.EXP.GNFS.CD", "parameter": "Exports of goods and services"},
                {"indicator": "NE.IMP.GNFS.CD", "parameter": "Imports of goods and services"},
                {"indicator": "NE.GDI.TOTL.CD", "parameter": "Investments"},
                {"indicator": "GC.DOD.TOTL.GD.ZS", "parameter": "Public debt"},
                {"indicator": "FP.CPI.TOTL", "parameter": "Consumer price indices"},
                {"indicator": "FR.INR.RINR", "parameter": "Interest rates"},
                # Add other requests for additional parameters here
            ]

            for param in parameters:
                data = fetch_indicator_data(country_id, param["indicator"])
                print(f"{param['parameter']}:\n{data}\n")

            print("============================")

    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:", e)

get_country_data()


