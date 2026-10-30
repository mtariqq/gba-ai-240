# Day6_Shenzhen_Client_Savings_Profit.py
# GBA Bulk Profit Calculator - Tariq from Mingora

clients = [
    {"name": "Mr. Li - Shenzhen", "deposit": 500000, "rate": 3.2},
    {"name": "Ms. Chen - Guangzhou", "deposit": 800000, "rate": 3.5},
    {"name": "Mr. Wong - Hong Kong", "deposit": 1200000, "rate": 4.0},
    {"name": "Ms. Zhang - Qianhai", "deposit": 300000, "rate": 2.8}
]

print("=== GBA DAILY PROFIT REPORT ===")
print("Date: Today | Bank: HSBC GBA\n")

total_profit = 0

for client in clients:
    # Profit Formula
    profit = client["deposit"] * client["rate"] / 100
    total_profit += profit
    
    # VIP Logic
    if profit > 30000:
        status = "VIP - Invite to Lounge"
    else:
        status = "Standard"

    print(f"{client['name']} | Deposit: {client['deposit']:,} | Profit: HKD {profit:,.0f} | {status}")

print(f"\n-----------------------------")
print(f"Total Clients: {len(clients)}")
print(f"Total Profit Payout Today: HKD {total_profit:,.0f}")
