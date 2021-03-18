student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


min=student_scores[0]
for i in student_scores:
  if i < min:
    min=i
print(f"The lowest score in the class is: {min}")

max = student_scores[0]
for a in student_scores:
  if a > max:
    max = a
print(f"The highest score in the class is: {max}")
