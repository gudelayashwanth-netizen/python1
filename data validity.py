
print("MOBILE PLAN COMPARISON")

usage = float(input("Enter your daily data usage: "))
days = int(input("Enter required validity days: "))
budget = int(input("Enter your budget: "))

price1 = 199
data1 = 1
validity1 = 28

price2 = 299
data2 = 1.5
validity2 = 56

price3 = 399
data3 = 2
validity3 = 84

best_price = 0
best_plan = ""

if data1 >= usage and validity1 >= days and price1 <= budget:
    best_price = price1
    best_plan = "Plan A"

if data2 >= usage and validity2 >= days and price2 <= budget:
    if best_price == 0 or price2 < best_price:
        best_price = price2
        best_plan = "Plan B"

if data3 >= usage and validity3 >= days and price3 <= budget:
    if best_price == 0 or price3 < best_price:
        best_price = price3
        best_plan = "Plan C"

if best_price > 0:
    print("Best Plan:", best_plan)
    print("Plan Price:", best_price)
else:
    print("No suitable plan available")
