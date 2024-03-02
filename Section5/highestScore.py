student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is {highest_score}")

lowest_score = 0
for score in student_scores:
    if score < highest_score :
        highest_score = score
        lowest_score = highest_score
print(f"The lowest score in the class is {lowest_score}")
