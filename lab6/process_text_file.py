def convert_grade_to_number(grade):
    grade_map = {
        'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0,
        'B-': 2.7, 'C': 2.0
    }
    return grade_map.get(grade, None)

def process_student_data(filename):
    students = []
    grades = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                clean_line = line.strip()
                if clean_line:
                    parts = clean_line.split(" - ")
                    name = parts[0]
                    grade = parts[2].replace("Grade: ", "")
                    students.append(name)

                    grade_value = convert_grade_to_number(grade)
                    if grade_value:
                        grades.append(grade_value)

        print("Total Students:", len(students))
        print("Average Grade:", sum(grades)/len(grades))

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    process_student_data("students.txt")
