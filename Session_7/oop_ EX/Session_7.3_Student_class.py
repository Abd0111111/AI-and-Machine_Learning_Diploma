# The code below shows how to keep name id and a list of courses in one object
# It explains how to add a new course to the list
# It explains how to show all details in one formatted line
# You can use this structure in any small system that needs basic student management

class Student:
    def __init__(self, name, student_id):     # creates a new student with name and id
        self.name = name                      # saves student name
        self.student_id = student_id          # saves student id
        self.courses = []                     # creates an empty list for courses

    def enroll(self, course):                 # adds a new course
        self.courses.append(course)           # stores the course in the list
        print(f"{self.name} has enrolled in {course}")   # prints enrollment message

    def display_info(self):                   # shows student data
        print(f"Student: {self.name}, ID: {self.student_id}, Courses: {', '.join(self.courses)}")
        # prints name id and all courses in one line

# Example usage
student1 = Student("John Doe", "S12345")      # creates a student object
student1.enroll("Math")                       # enrolls in first course
student1.enroll("Science")                    # enrolls in second course
student1.display_info()                       # prints student information