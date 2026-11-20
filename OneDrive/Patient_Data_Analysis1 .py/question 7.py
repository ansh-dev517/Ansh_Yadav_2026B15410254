print("Question 7: Count male and female patients")
print("Question: Write a Python program to count male and female patients.")
gender = [
    "Male", "Female", "Male", "Female", "Male",
    "Female", "Male", "Female", "Male", "Female"
]

male = 0
female = 0

for person in gender:

    if person == "Male":
        male = male + 1

    else:
        female = female + 1

print("Male Patients:", male)
print("Female Patients:", female)