# Request grades for six modules
module_1grade = float(input("Enter grade for Module 1: "))
module_2grade = float(input("Enter grade for Module 2: "))
module_3grade = float(input("Enter grade for Module 3: "))
module_4grade = float(input("Enter grade for Module 4: "))
module_5grade = float(input("Enter grade for Module 5: "))
module_6grade = float(input("Enter grade for Module 6: "))
# create list and add grades to list
gradeList = [module_1grade, module_2grade, module_3grade, module_4grade,
module_5grade, module_6grade]
# Determine what is the lowest, highest, sum and average
lowest = min(gradeList)
highest = max(gradeList)
total = sum(gradeList)
avg = sum(gradeList)/len(gradeList)
# Display the results
print("\n------------Results------------")
print(f'{"Lowest Grade:":<20}{lowest}')
print(f'{"Highest Grade:":<20}{highest}')
print(f'{"Sum of Grades:":<20}{total}')
print(f'{"Average:":<20}{avg:.2f}')
print("----------------------------------------")
print("Your grade is: ", end="")
if avg >= 90:
print("A")
elif avg >= 80:
print("B")
elif avg >= 70:
print("C")
elif avg >= 60:
print("D")
else:
print("F")
