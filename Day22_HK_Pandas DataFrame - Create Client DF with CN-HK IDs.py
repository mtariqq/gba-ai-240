import pandas as pd

# Day 22 - GBA Client DataFrame
clients = [
    {"ClientID": "C001", "Name": "Shenzhen Co 某某有限公司", "CN_ID": "440300123456", "HK_ID": "HK1234567", "BalanceHKD": 1200000, "Currency": "CNY", "Branch": "Qianhai", "RiskScore": 85},
    {"ClientID": "C002", "Name": "HK Trading Ltd", "CN_ID": None, "HK_ID": "HK2345678", "BalanceHKD": 400000, "Currency": "HKD", "Branch": "Central", "RiskScore": 30},
    {"ClientID": "C003", "Name": "Qianhai Ltd", "CN_ID": "440300789012", "HK_ID": "HK3456789", "BalanceHKD": 800000, "Currency": "CNY", "Branch": "Qianhai", "RiskScore": 65},
    {"ClientID": "C004", "Name": "Central HK Ltd", "CN_ID": None, "HK_ID": "HK4567890", "BalanceHKD": 200000, "Currency": "HKD", "Branch": "Central", "RiskScore": 20},
    {"ClientID": "C005", "Name": "Futian Export Co", "CN_ID": "440300345678", "HK_ID": "HK5678901", "BalanceHKD": 2500000, "Currency": "CNY", "Branch": "Shenzhen", "RiskScore": 92},
    {"ClientID": "C006", "Name": "Kowloon Retail Ltd", "CN_ID": None, "HK_ID": "HK6789012", "BalanceHKD": 950000, "Currency": "HKD", "Branch": "Kowloon", "RiskScore": 45},
]

df = pd.DataFrame(clients)
print(df)

print("--- Shape ---")
print(df.shape)  # (rows, columns)

print("--- First 3 rows ---")
print(df.head(3))

print("--- Columns ---")
print(df.columns.tolist())
