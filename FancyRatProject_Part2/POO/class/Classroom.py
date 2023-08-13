class Classroom:
    def __init__(self, name, teacher, students):
        self.name = name
        self.teacher = teacher
        self.students = students if students is not None else []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_students(self):
        return self.students.copy() # Return a copy to prevent direct modification

    def get_teacher(self):
        return self.teacher

    def get_class_info(self):
        student_names = [student.name for student in self.students]
        return f"Classroom '{self.name}' taught by {self.teacher.name} with students: {', '.join(student_names)}"