# Day 10 - GBA Currency Converter

hkd = 10000
print("You have:", hkd, "HKD")

# 1 HKD = 0.92 CNY (China money)
cny = hkd * 0.92
print("In China (CNY):", cny)

# 1 HKD = 0.13 USD (USA money)
usd = hkd * 0.13
print("In USA (USD):", usd)

# Is it enough for Shenzhen trip?
if cny > 5000:
    print("Enough for Shenzhen trip! ✅")
else:
    print("Not enough, need more HKD ❌")
