# Day8_GBA_VIP_Filter_Search.py
# GBA VIP Client Filter - Tariq from Mingora

clients = [
    {"name": "  tencent holdings ltd  ", "savings": 500000, "profit": 25000},
    {"name": "Alibaba Group Co., Ltd.", "savings": 150000, "profit": 7500},
    {"name": "  BYD COMPANY LIMITED ", "savings": 800000, "profit": 40000},
    {"name": "huawei technologies co., ltd", "savings": 90000, "profit": 4500},
    {"name": "  Mox Bank Limited ", "savings": 1200000, "profit": 60000},
    {"name": "  Tariq Bank Mingora Ltd  ", "savings": 300000, "profit": 15000},
]

print("=== GBA VIP CLIENTS (Savings >= 300,000) ===")

vip_count = 0
vip_total_profit = 0

for c in clients:
    # 1. Clean name (Day 7 skill)
    clean_name = c["name"].strip().replace("Holdings", "").replace("Group", "").replace("Co., Ltd.", "").replace("Company Limited", "").replace("Limited", "").replace("Ltd.", "").replace("Ltd", "").replace("technologies", "").upper()
    clean_name = " ".join(clean_name.split())

    # 2. Filter (Day 8 NEW skill)
    if c["savings"] >= 300000:
        print(f"VIP: {clean_name} | Savings: {c['savings']} | Profit: {c['profit']}")
        vip_count += 1
        vip_total_profit += c["profit"]
    else:
        print(f"Regular: {clean_name} | Savings: {c['savings']}")

print(f"\nTotal VIP Clients: {vip_count}")
print(f"Total VIP Profit: {vip_total_profit} HKD")
