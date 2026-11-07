# Day 9 - Hong Kong Loan Checker

customers = [
    ["Chan Tai Man", 35000],
    ["Ali Khan", 15000],
    ["Wong Mei Ling", 50000],
    ["Ahmed", 18000],
]

print("=== HSBC LOAN CHECK ===")

for name, salary in customers:
    if salary >= 20000:
        print(name, "- Salary:", salary, "- LOAN APPROVED ✅")
    else:
        print(name, "- Salary:", salary, "- LOAN REJECTED ❌")
