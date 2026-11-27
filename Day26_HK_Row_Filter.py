import pandas as pd

# Same GBA Clients - Day 26
data = {
    'ClientID': ['HK001', 'SZ002', 'HK003', 'GZ004', 'HK005', 'QH006', 'HK007'],
    'ClientName': ['Chan Tai Man', 'Li Wei', 'Wong Mei Ling', 'Zhang Min', 'Ho Ka Yee', 'Chen Hao', 'Lau Chi Keung'],
    'Branch': ['Central', 'Qianhai', 'Central', 'Guangzhou', 'Kowloon', 'Qianhai', 'Central'],
    'BalanceHKD': [2500000, 850000, 1200000, 450000, 3200000, 950000, 1800000],
    'RiskScore': [25, 78, 30, 85, 20, 72, 45],
    'Currency': ['HKD', 'CNY', 'HKD', 'CNY', 'HKD', 'CNY', 'HKD']
}

df = pd.DataFrame(data)
print("Full Data:")
print(df)
print("\n----------------\n")

# 1. Filter 1 - Only Balance > 1M
print("1. Balance > 1M HKD:")
print(df[df['BalanceHKD'] > 1000000])

print("\n----------------\n")

# 2. Filter 2 - Only Branch = Central
print("2. Branch = Central:")
print(df[df['Branch'] == 'Central'])

print("\n----------------\n")

# 3. Filter 3 - BOTH conditions - Today's main task
# & means AND, use ( ) around each condition
print("3. Balance > 1M AND Branch = Central:")
rich_central = df[(df['BalanceHKD'] > 1000000) & (df['Branch'] == 'Central')]
print(rich_central)

print("\n----------------\n")

# 4. Filter + Select Columns together
print("4. Final Manager Report - Only 3 columns:")
final_report = rich_central[['ClientID', 'BalanceHKD', 'RiskScore']]
print(final_report)
print(f"\nTotal clients found: {len(final_report)}")
