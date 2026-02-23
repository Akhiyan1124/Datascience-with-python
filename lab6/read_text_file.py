def read_student_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading student information:")
            print("-" * 40)

            for line_number, line in enumerate(file, start=1):
                clean_line = line.strip()
                if clean_line:
                    print(f"Line {line_number}: {clean_line}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    read_student_file("students.txt")
