# Day 24 - Inspect The Bank Portfolio
# GBA Bank - Check data before reporting to manager

import pandas as pd
import os

# 1. Check where we are and if file exists
print("Current folder:", os.getcwd())
print("File exists:", os.path.exists("gba_clients.csv"))

# 2. Load CSV
df = pd.read_csv("gba_clients.csv")

# 3. Clean the messy data
df = df.drop_duplicates()
df["Branch"] = df["Branch"].str.strip().str.title()
df["Currency"] = df["Currency"].str.strip().str.upper()
df["BalanceHKD"] = df["BalanceHKD"].astype(str).str.replace(",", "").str.strip()
df["BalanceHKD"] = pd.to_numeric(df["BalanceHKD"], errors="coerce").fillna(0)

# 4. Save clean version for next days
df.to_csv("gba_clients_clean.csv", index=False)

# 5. Inspect - First look
print("\n--- First 5 rows ---")
print(df.head())

print("\n--- Last 2 rows ---")
print(df.tail(2))

# 6. Inspect - Column types and missing values
print("\n--- Info ---")
print(df.info())

# 7. Inspect - Numbers summary (Manager tool)
print("\n--- Describe ---")
print(df.describe())

# 8. Inspect - Clients per Branch and Currency
print("\n--- Clients per Branch ---")
print(df["Branch"].value_counts())

print("\n--- Clients per Currency ---")
print(df["Currency"].value_counts())

# 9. Manager Summary
print("\n--- MANAGER SUMMARY ---")
print("Total Clients:", len(df))
print("Total BalanceHKD:", df["BalanceHKD"].sum())
print("Average BalanceHKD:", df["BalanceHKD"].mean())
print("Biggest Client Balance:", df["BalanceHKD"].max())

# 10. Biggest Client
print("\n--- Biggest Client ---")
print(df.sort_values("BalanceHKD", ascending=False).head(1))

# 11. High Risk Check
print("\n--- High Risk Clients (RiskScore > 80) ---")
print(df[df["RiskScore"] > 80])
print("High-risk Total Exposure:", df[df["RiskScore"] > 80]["BalanceHKD"].sum())
