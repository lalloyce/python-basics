# Class to manage student information and grades
class Student:
    # Class Attribute (shared by all students)
    school_name = "Python High School"
    total_students = 0

    # Constructor Method (runs when creating a new student)
    def __init__(self, name, age, grade):
        # Instance Attributes (unique to each student)
        self.name = name  # each student has their own name
        self.age = age  # each student has their own age
        self.grade = grade  # each student has their own grade
        self.scores = []  # list to store test scores

        # Increment total_students when a new student is created
        Student.total_students += 1

    # Regular Instance Method (needs self to access instance attributes)
    def add_score(self, score):
        self.scores.append(score)
        return f"Added score of {score} for {self.name}"

    # Another Instance Method
    def get_average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

    # Class Method (works with class attributes)
    @classmethod
    def get_total_students(cls):
        return f"Total number of students: {cls.total_students}"

    # Static Method (doesn't need self or cls)
    @staticmethod
    def is_passing_grade(score):
        return score >= 60


# Creating student objects
print("Creating students...")
alice = Student("Alice", 15, 10)  # name, age, grade
bob = Student("Bob", 16, 10)

# Using instance methods
print("\nAdding scores for students...")
print(alice.add_score(85))
print(alice.add_score(92))
print(bob.add_score(78))
print(bob.add_score(85))

# Getting individual student information
print("\nStudent averages:")
print(f"{alice.name}'s average score: {alice.get_average()}")
print(f"{bob.name}'s average score: {bob.get_average()}")

# Using class method
print("\nClass information:")
print(Student.get_total_students())

# Using static method
print("\nChecking if scores are passing grades...")
test_score = 75
print(f"Is {test_score} a passing grade? {Student.is_passing_grade(test_score)}")

# Accessing class and instance attributes
print("\nSchool information:")
print(f"School name: {Student.school_name}")
print(f"Alice's grade level: {alice.grade}")
print(f"Bob's grade level: {bob.grade}")