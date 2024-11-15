
maths = 50
english = 60
kiswahili = 70
physics = 80
chemistry = 90
biology = 100
geography = 40
history = 30

total = maths + english + kiswahili + physics + chemistry + biology + geography + history
avg = total / 8


if avg <39 and avg > 0:
    grade = "D"
elif avg < 59:
    grade = "C"
elif avg < 69:
    grade = "B"
else:
    grade = "A"

print(f"The average is {avg}, total is {total} and the grade is {grade}.")
