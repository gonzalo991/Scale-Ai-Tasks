class Student:
    def __init__(self, name, surname, grade_level):
        self.name = name
        self.surname = surname
        self.grade_level = grade_level
        self.qualifications = {} # Dictionary to store the student's qualifications

    def add_qualifications(self, subject, qualifications):
        self.qualifications[subject] = qualifications

    def display_qualifications(self):
        for subject, qualifications in self.qualifications.items():
            print(f"{self.name}'s qualifications in {subject}:")
            for qual in qualifications.items():
                print(f"{qual[0]}: {qual[1]}")