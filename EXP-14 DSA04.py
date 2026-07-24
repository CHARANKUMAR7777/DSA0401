# Study Time and Exam Score Correlation

study_time = [1, 2, 3, 4, 5, 6, 7, 8]
exam_score = [35, 45, 50, 60, 70, 80, 90, 95]

n = len(study_time)

# Calculate means
mean_x = sum(study_time) / n
mean_y = sum(exam_score) / n

# Calculate Pearson Correlation
numerator = 0
denominator_x = 0
denominator_y = 0

for i in range(n):
    numerator += (study_time[i] - mean_x) * (exam_score[i] - mean_y)
    denominator_x += (study_time[i] - mean_x) ** 2
    denominator_y += (exam_score[i] - mean_y) ** 2

correlation = numerator / ((denominator_x * denominator_y) ** 0.5)

print("Study Time (Hours):", study_time)
print("Exam Scores:", exam_score)
print("Correlation Coefficient:", round(correlation, 2))

if correlation > 0:
    print("Positive Correlation: As study time increases, exam scores increase.")
elif correlation < 0:
    print("Negative Correlation: As study time increases, exam scores decrease.")
else:
    print("No Correlation.")
