PMT = float(input("Enter Payment per Period:"))
R = float(input("Enter Annual Interest rate(%):")) / 100
T = float(input("Enter Time(in years):"))
n = int(input("Enter Number of Payments per year:"))

A = PMT * (( 1 + (R / n)) ** (n * T) - 1) / (R /n)
print(f"The accumulated amount after {T} years is: {A:.2f}")

