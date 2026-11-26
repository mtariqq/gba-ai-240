import pandas as pd

# GBA Clients - Day 25
data = {
    'ClientID': ['HK001', 'SZ002', 'HK003', 'GZ004', 'HK005', 'QH006'],
    'ClientName': ['Chan Tai Man', 'Li Wei', 'Wong Mei Ling', 'Zhang Min', 'Ho Ka Yee', 'Chen Hao'],
    'Branch': ['Central', 'Qianhai', 'Central', 'Guangzhou', 'Kowloon', 'Qianhai'],
    'BalanceHKD': [2500000, 850000, 1200000, 450000, 3200000, 950000],
    'RiskScore': [25, 78, 30, 85, 20, 72],
    'Currency': ['HKD', 'CNY', 'HKD', 'CNY', 'HKD', 'CNY']
}

df = pd.DataFrame(data)
print("Full Data:")
print(df)
print("\n----------------\n")

# 1. Select ONE column
print("1. Only Balance:")
print(df['BalanceHKD'])

print("\n----------------\n")

# 2. Select 3 columns - Today's main task
print("2. Manager Report - Only 3 columns:")
manager_report = df[['ClientID', 'BalanceHKD', 'RiskScore']]
print(manager_report)

print("\n----------------\n")

# 3. Select + Rename for manager
print("3. Clean Report for Manager:")
clean_report = df[['ClientID', 'BalanceHKD', 'RiskScore']].copy()
clean_report.columns = ['ID', 'Balance (HKD)', 'Risk']
print(clean_report)
