def uppercase_grades(student_grades):
    '''
    Function that receives a dictionary with the subjects and grades of a student and returns another dictionary with the subjects in uppercase and the grades corresponding to the grades.
    Parameters:
        student_grades: A dictionary with the subjects and grades of a student.
    Returns:
        A dictionary with the subjects in uppercase and the grades corresponding to the grades.
    '''
    return {
        subject.upper(): grade
        for subject, grade in student_grades.items()
    }

# Example usage of the uppercase_grades function

# Define a dictionary with the subjects and grades of a student
student_grades = {
    'math': 90,
    'science': 80,
    'history': 70,
    'literature': 80,
    'art': 90
}

# Apply the uppercase_grades function to the student_grades dictionary
uppercase_grades = uppercase_grades(student_grades)

# Print the uppercase_grades dictionary
print(uppercase_grades)