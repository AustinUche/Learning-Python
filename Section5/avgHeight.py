student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_heights = 0
for height in student_heights:
    total_heights += height
print(total_heights)

num_students = 0
for number in student_heights:
    num_students += 1
print(num_students)

avg_students = round(total_heights / num_students)
print(avg_students)

