P = float(input("Enter Principal Amount:"))
R = float(input("Enter Annual Interest rate(%):")) / 100
T = float(input("Enter Time(in years):"))
n = int(input("Enter Number of Times Interest Compouded per year:"))

A = P * (1 + (R / n)) ** (n * T)

print(f"The Total amount after {T} years is : {A:.2f}")