# Input the number of students
num_students = int(input())

# Create a dictionary to store the student names and their scores
student_scores = {}

# Input the student data
for _ in range(num_students):
    data = input().split()
    student_name = data[0]
    scores = list(map(float, data[1:]))
    student_scores[student_name] = scores

# Input the name of the student you want to find the average for
target_student = input()

# Calculate the average score for the target student
if target_student in student_scores:
    scores = student_scores[target_student]
    average_score = sum(scores) / len(scores)
    print("{:.2f}".format(average_score))
else:
    print("Student not found")
