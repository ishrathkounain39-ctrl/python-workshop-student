class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display()
