print("Question 6: Count patients in different age groups")
print("Question: Divide patients into three age groups:")
print("- Children: below 18")
print("- Adults: 18 to 59")
print("- Senior citizens: 60 and above")
ages = [25, 45, 12, 60, 32, 8, 70, 22, 55, 35]

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

print("Children:", children)
print("Adults:", adults)
print("Senior Citizens:", senior)