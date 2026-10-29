
print("HOSPITAL BILLING SYSTEM")

consultation = int(input("Enter consultation charges: "))
diagnostic = int(input("Enter diagnostic charges: "))
treatment = int(input("Enter treatment charges: "))

total = consultation + diagnostic + treatment
print("Total Bill:", total)
if total >= 3000:
    discount = 500
else:
    discount = 0
final_bill = total - discount
if final_bill >= 3000:
    category = "Full Payment"
else:
    category = "Concession Payment"
print("Discount:", discount)
print("Final Bill:", final_bill)
print("Patient Category:", category)
