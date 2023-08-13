class Teacher:
    def __init__(self, name, surname, subject, grade_level):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.grade_level = grade_level

    def get_grade_level(self):
       return self.grade_level

    # Method to qualify a student with specific qualifications
    def qualify_student(self, student, qualifications):
       # Check if qualifications are provided as a dictionary
       if not isinstance(qualifications, dict):
           raise ValueError("Qualifications should be provided as a dictionary.")
        
       # Call the student's add_qualifications method to add qualifications for the student
       student.add_qualifications(self.subject, qualifications)
        
        # Print the qualification information
       print(f"{self.name} {self.surname} qualified {student.name} in {self.subject} with the following qualifications:")
       for subject, qualification in qualifications.items():
            print(f"{subject}: {qualification}")