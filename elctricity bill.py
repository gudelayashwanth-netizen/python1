
# Electricity Billing System

units1 = int(input("Enter Month 1 units: "))
units2 = int(input("Enter Month 2 units: "))
units3 = int(input("Enter Month 3 units: "))
units = [units1, units2, units3]
bills = []

for i in range(3):
    print("\nMonth", i + 1)
    print("Units:", units[i])

    if units[i] <= 100:
        bill = units[i] * 2
    elif units[i] <= 200:
        bill = 200 + (units[i] - 100) * 3
    else:
        bill = 500 + (units[i] - 200) * 5
    print("Energy charge:", bill)
    bill = bill + 50
    print("Fixed charge: 50")
    surcharge = bill * 0.05
    bill = bill + surcharge
    print("Surcharge:", round(surcharge, 2))
    if units[i] <= 100:
        rebate = bill * 0.10
    else:
        rebate = 0
    bill = round(bill - rebate, 2)
    print("Rebate:", round(rebate, 2))
    print("Final bill: Rs.", bill)
    bills.append(bill)
print("\n--- Monthly Comparison ---")
print("Month 1 bill:", bills[0])
print("Month 2 bill:", bills[1])
print("Month 3 bill:", bills[2])
if bills[1] > bills[0] * 1.5:
    print("Unusual increase in Month 2")
if bills[2] > bills[1] * 1.5:
    print("Unusual increase in Month 3")
