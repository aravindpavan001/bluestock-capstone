import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

try:
    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_data = data['data']

        df = pd.DataFrame(nav_data)

        print(df.head())

        df.to_csv("data/raw/hdfc_top100_nav.csv", index=False)

        print("NAV data saved successfully!")

    else:
        print("Failed to fetch data")

except Exception as e:
    print("Error:", e)