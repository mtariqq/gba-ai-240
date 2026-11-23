# Day 20 - GBA Remittance Flagger
# Repo: banking-ai-foundation

def calculate_gba_profit(cny, rate, years):
    # Day 19 - Function
    return cny * rate * years

def check_risk(amount_hkd, country, has_default):
    # Day 13, 14, 15 - If + Boolean + if-elif-else
    if amount_hkd > 1000000 and country == "CN":
        return "High"
    elif amount_hkd > 500000 or has_default == True:
        return "Medium"
    else:
        return "Low"

# Day 3 - List of 7-day GBA transactions
transactions = [
    {"client": "Shenzhen Co 某某有限公司", "amount_hkd": 1200000, "country": "CN", "default": False},
    {"client": "HK Trading Ltd", "amount_hkd": 400000, "country": "HK", "default": False},
    {"client": "Qianhai Ltd", "amount_hkd": 800000, "country": "CN", "default": True},
    {"client": "Central HK Ltd", "amount_hkd": 200000, "country": "HK", "default": False},
    {"client": "Futian Export Co", "amount_hkd": 2500000, "country": "CN", "default": False},
]

# Day 17 - For loop to flag all
print("--- GBA High-Risk Flagger ---")
high_count = 0

for tx in transactions:
    risk = check_risk(tx["amount_hkd"], tx["country"], tx["default"])
    print(tx["client"], "|", tx["amount_hkd"], "HKD | Risk:", risk)
    
    if risk == "High":
        print("  -> FLAG FOR HKMA AML REVIEW - EDD Required")
        high_count = high_count + 1

print("--- Summary ---")
print("Total transactions:", len(transactions))
print("High-risk flagged:", high_count)

# Day 19 function test
print("Profit on 100,000 CNY at 15% for 2 years:", calculate_gba_profit(100000, 0.15, 2))
