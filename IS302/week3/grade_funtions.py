def calculate_average(g1, g2, g3):
    return (g1 + g2 + g3) / 3

def get_remark(average):
    if 90 <= average <= 100:
        return "Excellent"
    elif 85 <= average <= 89:
        return "Very Good"
    elif 80 <= average <= 84:
        return "Good"
    elif 75 <= average <= 79:
        return "Fair"
    else:
        return "Failed"

# Input grades
grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))

# Compute average
avg = calculate_average(grade1, grade2, grade3)

# Get remark
remark = get_remark(avg)

# Output
print("\n----- STUDENT GRADE RESULT -----")
print("Average:", round(avg, 2))
print("Remark:", remark)