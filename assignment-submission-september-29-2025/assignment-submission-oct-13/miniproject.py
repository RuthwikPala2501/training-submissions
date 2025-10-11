# ----- Using Python Data Structures -----
# list, dict, set, tuple, Counter

from collections import Counter

# 1️⃣ List – to store student names
students = ["Roy", "Wick", "John"]

# 2️⃣ Dictionary – to store marks of each student
marks = {
    "Roy": {"Math": 88, "Science": 92, "English": 80},
    "Wick": {"Math": 95, "Science": 90, "English": 85},
    "John": {"Math": 75, "Science": 70, "English": 78}
}

# 3️⃣ Set – to find all unique subjects
subjects = set()
for m in marks.values():
    subjects.update(m.keys())

# 4️⃣ Tuple – store class info (fixed data)
class_info = ("Grade 10", "Section A")

# 5️⃣ Calculate average marks using dict
average_marks = {}
for name, score in marks.items():
    average_marks[name] = sum(score.values()) / len(score)

# 6️⃣ Find the top scorer
top_student = max(average_marks, key=average_marks.get)

# 7️⃣ Count how many students got high marks (>90) in each subject
high_score_count = Counter()
for name, score in marks.items():
    for subject, mark in score.items():
        if mark >= 90:
            high_score_count[subject] += 1

# ----- Output -----
print("Class Info:", class_info)
print("Students:", students)
print("Subjects:", subjects)
print("Average Marks:", average_marks)
print("Top Scorer:", top_student, "with", average_marks[top_student], "average")
print("High Scorers by Subject:", dict(high_score_count))
