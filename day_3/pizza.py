# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size.upper() == "S":
    bill += 15
elif size.upper() == "M":
    bill += 20
elif size.upper() == "L":
    bill += 25
else:
    print('Please enter "S", "M" or "L" only.')

if add_pepperoni.upper() == "Y":
    if size.upper() == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese.upper() == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")


# amt_s = 15
# amt_m = 20
# amt_l = 25
# amt_pep_s = 2
# amt_pep_m_l = 3
# amt_ex_cheese = 1


# if size.upper() == "S":
#     amt = amt_s
#     if add_pepperoni.upper() == "Y":
#         amt += amt_pep_s
#         if extra_cheese.upper() == "Y":
#             amt += amt_ex_cheese
#             print(f"Your final bill is: ${amt}")
#         else:
#             print(f"Your final bill is: ${amt}") # Small Pizza Without Cheese
#     else:
#         print(f"Your final bill is: ${amt}") # Small Pizza  Without Pepperoni
# elif size.upper() == "M":
#     amt = amt_m
#     if add_pepperoni.upper() == "Y":
#         amt += amt_pep_m_l
#         if extra_cheese.upper() == "Y":
#             amt += amt_ex_cheese
#             print(f"Your final bill is: ${amt}")
#         else:
#             print(f"Your final bill is: ${amt}") # Medium Pizza Without Cheese
#     else:
#         print(f"Your final bill is: ${amt}") # Medium Pizza Without Pepperoni
# else:
#     amt = amt_l
#     if add_pepperoni.upper() == "Y":
#         amt += amt_pep_m_l
#         if extra_cheese.upper() == "Y":
#             amt += amt_ex_cheese
#             print(f"Your final bill is: ${amt}")
#         else:
#             print(f"Your final bill is: ${amt}") # Large Pizza Without Cheese
#     else:
#         print(f"Your final bill is: ${amt}") # Large Pizza Without Pepperoni
