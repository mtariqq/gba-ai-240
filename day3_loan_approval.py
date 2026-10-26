# Day 3: Hong Kong GBA Bank - Loan Approval System
# Mingora to Hong Kong - Decision Power

customer_name = "Muhammad Tariq"
monthly_income_hkd = 45000  # Your future HK income
credit_score = 720
loan_amount_hkd = 200000

print(f"Customer: {customer_name}")
print(f"Applying for loan: {loan_amount_hkd} HKD")
print("--- Bank Decision ---")

# Bank Rule 1: Income must be > 30,000 HKD
# Bank Rule 2: Credit score must be > 700

if monthly_income_hkd >= 30000 and credit_score >= 700:
    print("✅ LOAN APPROVED - Welcome to GBA Hong Kong!")
    print(f"Approved Amount: {loan_amount_hkd} HKD")
else:
    print("❌ LOAN REJECTED - Improve income/credit score")
    if monthly_income_hkd < 30000:
        print(f"Reason: Income {monthly_income_hkd} is low. Need 30000+")
    if credit_score < 700:
        print(f"Reason: Credit Score {credit_score} is low. Need 700+")

# Bonus: Your profit from this loan (Bank earns 8% interest)
bank_profit = loan_amount_hkd * 0.08
print(f"\nBank Profit from this loan: {bank_profit} HKD")
