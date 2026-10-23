# Day 1 - GBA Profit Calculator - Your Name - 2026-05-13

# --- Input from our Shenzhen client ---
initial_cny = 1000000  # 1 Million CNY
annual_rate = 0.12     # 12% return in HK fund
years = 5              # 5 year plan

# --- Calculation - Compound Interest ---
future_value_cny = initial_cny * (1 + annual_rate) ** years
profit_cny = future_value_cny - initial_cny

# --- Convert to HKD for HK reporting ---
# Today's rate: 1 CNY = 1.08 HKD (you can change later)
cny_to_hkd_rate = 1.08
profit_hkd = profit_cny * cny_to_hkd_rate
future_value_hkd = future_value_cny * cny_to_hkd_rate

# --- Print Report like you did in branch ---
print("=== GBA Client Profit Report ===")
print(f"Client Location: Shenzhen")
print(f"Investment Location: Hong Kong")
print(f"Initial Amount: {initial_cny} CNY")
print(f"Duration: {years} years at {annual_rate*100}%")
print(f"-------------------------------")
print(f"Future Value: {round(future_value_cny)} CNY / {round(future_value_hkd)} HKD")
