print("FOOD WASTE MONITORING SYSTEM")

days = int(input("Enter number of days: "))
limit = 10

for i in range(days):

    print("\nDay", i + 1)

    prepared = int(input("Enter food prepared: "))
    served = int(input("Enter food served: "))
    leftover = prepared - served
    wastage = (leftover / prepared) * 100

    print("Leftover food:", leftover)
    print("Food wastage:", wastage, "%")

    if wastage > limit:
        print("High food wastage!")
    else:
        print("Food wastage is under control.")