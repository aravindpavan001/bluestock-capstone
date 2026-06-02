import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master['amfi_code'].unique())
nav_codes = set(nav_history['amfi_code'].unique())

missing_codes = fund_codes - nav_codes

print("\nTotal AMFI Codes in Fund Master:", len(fund_codes))
print("Total AMFI Codes in NAV History:", len(nav_codes))

if len(missing_codes) == 0:
    print("\nAll AMFI codes from fund_master exist in nav_history.")
else:
    print("\nMissing AMFI Codes:")
print(missing_codes)
