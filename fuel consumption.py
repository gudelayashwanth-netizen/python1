print("FUEL COST COMPARISON")
distance = float(input("Enter journey distance in km: "))
price = 105
reserve = 2

bike = 40
car = 20
suv = 12


bike_fuel = distance / bike
bike_total = bike_fuel + reserve
bike_cost = bike_total * price


car_fuel = distance / car
car_total = car_fuel + reserve
car_cost = car_total * price

suv_fuel = distance / suv
suv_total = suv_fuel + reserve
suv_cost = suv_total * price

print("Bike Cost:", bike_cost)
print("Car Cost:", car_cost)
print("SUV Cost:", suv_cost)
if bike_cost <= car_cost and bike_cost <= suv_cost:
    print("Lowest Cost Vehicle: Bike")
    print("Total Fuel Required:", bike_total)

elif car_cost <= suv_cost:
    print("Lowest Cost Vehicle: Car")
    print("Total Fuel Required:", car_total)

else:
    print("Lowest Cost Vehicle: SUV")
    print("Total Fuel Required:", suv_total)
