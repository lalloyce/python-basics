def grading():
    name = input("What is your name? ")
    print(f"Hello {name}, enter your marks for the following 5 subjects:")

    # Function to check valid marks
    def get_marks(subject):
        while True:
            try:
                marks = int(input(f"{subject}: "))
                if 0 <= marks <= 100:
                    return marks
                else:
                    print("Invalid marks. Please enter a number between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    maths = get_marks("Maths")
    english = get_marks("English")
    kiswahili = get_marks("Kiswahili")
    physics = get_marks("Physics")
    chemistry = get_marks("Chemistry")

    total = maths + english + kiswahili + physics + chemistry
    average = total / 5

    if 0 <= average < 39:
        grade = "D"
    elif 39 <= average < 59:
        grade = "C"
    elif 59 <= average < 69:
        grade = "B"
    elif 69 <= average <= 100:
        grade = "A"
    else:
        print("Invalid average marks. Something went wrong.")
        return

    print(f"Hello {name}, your average is {average:.2f}, total is {total}, and your grade is {grade}.")

grading()
