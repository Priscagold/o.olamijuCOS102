# Program to determine Annual Tax Revenue (ATR)

# Input years of experience and age
experience = int(input("Enter staff's years of experience: "))
age = int(input("Enter staff's age: "))

# Determine ATR based on conditions
if experience > 25 and age >= 55:
    atr = 5600000
elif experience > 20 and age >= 45:
    atr = 4480000
elif experience > 10 and age >= 35:
    atr = 1500000
else:
    atr = 550000

# Output the result
print(f"Annual Tax Revenue (ATR) is: ₦{atr:,.2f}")