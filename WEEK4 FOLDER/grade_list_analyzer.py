grades = []

for i in range(5):
    grade = float(input(f"Enter grade {i+1}: "))
    grades.append(grade)

average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)

print("\nResults:")
print("Average Grade:", average)
print("Highest Grade:", highest)
print("Lowest Grade:", lowest)