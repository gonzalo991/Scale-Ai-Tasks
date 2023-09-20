students = {
    "Tom": [0, 10, 30, 40],
    "Jerry": [0, 5, 30, 60],
    "Lily": [0, 20, 40, 60],
    "Adam": [0, 10, 40, 60],
    "Sam": [0, 10, 20, 40]
}

for student_name, grades in students.items():
    if grades:  # Check if the list of grades is not empty
        try:
            # Check if all elements in the grades list are numeric
            if all(isinstance(grade, (int, float)) for grade in grades):
                summatory = sum(grades)  # Calculate the sum of grades
                grades_average = summatory / len(grades)  # Calculate the average

                print(f"The average of {student_name} is: {grades_average}")

                if grades_average >= 60:
                    print(f"{student_name} has passed the subject")
                else:
                    print(f"{student_name} has not passed the subject")
            else:
                print(f"{student_name}'s grades list contains non-numeric values.")
        except ZeroDivisionError as ze:
            print(f"An error has occurred: {ze}")
    else:
        print(f"{student_name}'s grades list is empty, unable to calculate the average.")
