def sort_students(student_list):
    # Sort the student_list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students
#Now, let's create some sample student objects and test the 'sort_students' function:
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Sample student objects
students = [
    Student("Dhanush", "22001", 3.5),
    Student("Praveen", "22002", 4.5),
    Student("Gowtham", "22003", 4.0),
    Student("Dhilip", "22004", 3.9),
]

# Sort the students based on CGPA
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
  