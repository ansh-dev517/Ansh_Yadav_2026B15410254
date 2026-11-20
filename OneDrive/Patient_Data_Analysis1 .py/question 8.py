print("Question 8: Count patients department-wise")
print("Question: Write a program to calculate the number of patients in each department.")
department = [
    "Medicine", "Cardiology", "Pediatrics",
    "Orthopedics", "Medicine", "Pediatrics",
    "Cardiology", "Dermatology", "Medicine",
    "Orthopedics"
]

medicine = 0
cardiology = 0
pediatrics = 0
orthopedics = 0
dermatology = 0

for dept in department:

    if dept == "Medicine":
        medicine = medicine + 1

    elif dept == "Cardiology":
        cardiology = cardiology + 1

    elif dept == "Pediatrics":
        pediatrics = pediatrics + 1

    elif dept == "Orthopedics":
        orthopedics = orthopedics + 1

    elif dept == "Dermatology":
        dermatology = dermatology + 1

print("Medicine:", medicine)
print("Cardiology:", cardiology)
print("Pediatrics:", pediatrics)
print("Orthopedics:", orthopedics)
print("Dermatology:", dermatology)