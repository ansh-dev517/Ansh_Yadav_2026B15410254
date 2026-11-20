print("Question 10: Generate a complete patient analysis report")
print("Question: Write a Python program to display the total patients,/n")
print(" average age, youngest patient, oldest patient, age group analysis and gender analysis.")
# Patient Data Analysis Project

ages = [25, 45, 12, 60, 32, 8, 70, 22, 55, 35]

gender = [
    "Male", "Female", "Male", "Female", "Male",
    "Female", "Male", "Female", "Male", "Female"
]

# Total patients
total_patients = len(ages)

# Average age
average_age = sum(ages) / total_patients

# Youngest and oldest
youngest = min(ages)
oldest = max(ages)

# Age groups
children = 0
adults = 0
senior = 0

for age in ages:

    if age < 18:
        children = children + 1

    elif age < 60:
        adults = adults + 1

    else:
        senior = senior + 1

# Gender count
male = 0
female = 0

for person in gender:

    if person == "Male":
        male = male + 1

    else:
        female = female + 1

# Final report
print("===== PATIENT DATA ANALYSIS =====")

print("Total Patients:", total_patients)
print("Average Age:", average_age)
print("Youngest Patient:", youngest)
print("Oldest Patient:", oldest)

print("\nAge Group Analysis")
print("Children:", children)
print("Adults:", adults)
print("Senior Citizens:", senior)

print("\nGender Analysis")
print("Male Patients:", male)
print("Female Patients:", female)