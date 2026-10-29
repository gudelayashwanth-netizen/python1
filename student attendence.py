
print("ATTENDANCE RECOVERY CALCULATOR")
total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))
required = float(input("Enter required attendance percentage: "))

if total <= 0 or attended < 0 or attended > total or required <= 0 or required > 100:
    print("Invalid input")
else:
    current = (attended / total) * 100
    print("Current Attendance:", current, "%")
    if current >= required:
        print("You are already eligible")
    else:
        future = 0

        while ((attended + future) / (total + future)) * 100 < required:
            future = future + 1
        print("Minimum classes to attend:", future)
        print("You will reach the required attendance")
