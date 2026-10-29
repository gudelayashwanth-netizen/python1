# student Scholarship System
name = input("Enter student name: ")
mark1 = int(input("Enter subject 1 marks: "))
mark2 = int(input("Enter subject 2 marks: "))
mark3 = int(input("Enter subject 3 marks: "))
attendance = float(input("Enter attendance percentage: "))
income = int(input("Enter family income: "))

total = mark1 + mark2 + mark3
aggregate = total / 3

print("\n========== STUDENT DETAILS ==========")
print("Student name:", name)
print("Subject 1 marks:", mark1)
print("Subject 2 marks:", mark2)
print("Subject 3 marks:", mark3)
print("Total marks:", total, "out of 300")
print("Aggregate:", aggregate, "%")
print("Attendance:", attendance, "%")
print("Family income: Rs.", income)
if (aggregate >= 75 and mark1 >= 60 and mark2 >= 60 and mark3 >= 60 and attendance >= 75 and income <= 500000):
    print("Result: Eligible for scholarship")
else:
    print("Result: Not eligible for scholarship")
