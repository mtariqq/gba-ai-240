# Day 4: Hong Kong GBA Bank - Customer Grades & Bulk Processing
# GBA AI 240 - Mingora to Hong Kong

customers = [
    {"name": "Tariq - Mingora", "income": 45000, "credit": 720},
    {"name": "Ali - GBA", "income": 28000, "credit": 680},
    {"name": "Chen - Hong Kong", "income": 80000, "credit": 800},
    {"name": "Ayesha - Future Banker", "income": 55000, "credit": 750}
]

print("--- GBA Hong Kong Daily Loan Report ---")
total_approved = 0
total_profit = 0

for customer in customers:
    name = customer["name"]
    income = customer["income"]
    credit = customer["credit"]
    
    # Grading system with if-elif-else
    if income >= 70000 and credit >= 800:
        grade = "VIP - Instant Approval"
        approved = 500000
    elif income >= 40000 and credit >= 700:
        grade = "Gold - Approved"
        approved = 200000
    elif income >= 30000 and credit >= 650:
        grade = "Silver - Small Loan"
        approved = 50000
    else:
        grade = "Rejected - Need Improvement"
        approved = 0
    
    print(f"\nCustomer: {name} | Income: {income} HKD | Credit: {credit}")
    print(f"Grade: {grade} | Loan: {approved} HKD")
    
    if approved > 0:
        total_approved += approved
        total_profit += approved * 0.08

print("\n--- End of Day Report ---")
print(f"Total Loans Approved: {total_approved} HKD")
print(f"Total Bank Profit (8%): {total_profit} HKD")
print(f"Your Progress: Day 4/240 - Future 100K HKD Banker!")
