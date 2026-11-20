print("Question 9: Count patients according to blood group")
print("Question: Write a Python program to count patients having different blood groups.")
blood_group = [
    "O+", "B+", "A+", "O+", "AB+",
    "B+", "O-", "A+", "B-", "O+"
]

o_positive = 0
b_positive = 0
a_positive = 0
ab_positive = 0
o_negative = 0
b_negative = 0

for blood in blood_group:

    if blood == "O+":
        o_positive = o_positive + 1

    elif blood == "B+":
        b_positive = b_positive + 1

    elif blood == "A+":
        a_positive = a_positive + 1

    elif blood == "AB+":
        ab_positive = ab_positive + 1

    elif blood == "O-":
        o_negative = o_negative + 1

    elif blood == "B-":
        b_negative = b_negative + 1

print("O+:", o_positive)
print("B+:", b_positive)
print("A+:", a_positive)
print("AB+:", ab_positive)
print("O-:", o_negative)
print("B-:", b_negative)