P = float(input("Enter Principal Amount: "))
R = float(input("Enter Annual Interest Rate(%): "))
T = float(input("Enter Time (in years): "))

A = P * (1 + (R / 100) * T)

print(f"The total amount after {T} years is: {A:.2f}")
