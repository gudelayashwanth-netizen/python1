print("SMART PARKING FEE SYSTEM")
vehicle = input("Enter vehicle type (bike/car/bus): ").lower()
entry = int(input("Enter entry hour (0-23): "))
exit = int(input("Enter exit hour (0-23): "))

if entry < 0 or entry > 23 or exit < 0 or exit > 23:
    print("Invalid time")

elif entry == exit:
    print("Invalid parking time")

else:
    if vehicle == "bike":
        rate = 10
    elif vehicle == "car":
        rate = 20
    elif vehicle == "bus":
        rate = 40
    else:
        rate = 0
    if rate == 0:
        print("Invalid vehicle type")

    else:
        if exit < entry:
            hours = (24 - entry) + exit
            overnight = 1
        else:
            hours = exit - entry
            overnight = 0

        fee = hours * rate

        if fee < 20:
            fee = 20
        if fee > 200:
            fee = 200
        if overnight == 1:
            fee = fee + 50
        print("Vehicle:", vehicle)
        print("Parking Hours:", hours)
        print("Overnight:", overnight)
        print("Final Parking Fee:", fee)
