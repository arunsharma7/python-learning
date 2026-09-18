temp = 15
if temp > 30:
    print("first stement")
    print("Drink water")  # Ensure this is exactly 4 spaces
elif temp > 20:
    print("It's nice")
else:
    print("it's cold")
print("done")


age = 12
if age >= 18:
    message = "Eleigible"
else:
    message= "not eligible"

message1 = "Eligible" if age >=18 else "Not Eligible"

print(message, message1)


#and or and not

high_income = False
good_credit = True
student = False

#if (high_income or good_credit) and not student:
if high_income and good_credit and not student:
    print("Eligible")
else:
    print("not eligible")