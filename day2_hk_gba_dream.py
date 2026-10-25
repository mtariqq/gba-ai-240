# Day 2 - REVISED for Hong Kong Dream
customer_name = "Future You"
account_balance = 100000  # HKD - Hong Kong Dollars
interest_rate = 4.2       # Hong Kong bank rate
is_premium = True
branch = "Hong Kong - Greater Bay Area"
city_target = "Schengen"

print(f"Customer: {customer_name}")
print(f"Target Branch: {branch}")
print(f"Balance: {account_balance} HKD")
print(f"Goal: {city_target} in 1 year")

profit = (account_balance * interest_rate) / 100
print(f"Yearly Profit in HK: {profit} HKD")
