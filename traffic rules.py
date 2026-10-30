print("TRAFFIC VIOLATION PENALTY CALCULATOR")
fine = 0
count = 0
n = int(input("Enter number of violations: "))
for i in range(n):
    print("\n1. No Helmet")
    print("2. No Licence")
    print("3. Using Mobile")

    offence = int(input("Enter offence number: "))
    repeat = input("Is it a repeat offence? (yes/no): ").lower()

    if offence == 1:
        if repeat == "yes":
            fine = fine + 1000
        else:
            fine = fine + 500

        count = count + 1

    elif offence == 2:
        if repeat == "yes":
            fine = fine + 2000
        else:
            fine = fine + 1000

        count = count + 1

    elif offence == 3:
        if repeat == "yes":
            fine = fine + 3000
        else:
            fine = fine + 1500

        count = count + 1

    else:
        print("Invalid offence")

print("\nTRAFFIC PENALTY SUMMARY")
print("Total Fine:", fine)
print("Total Violations:", count)
if count >= 2:
    print("Disqualification: Yes")
else:
    print("Disqualification: No")
