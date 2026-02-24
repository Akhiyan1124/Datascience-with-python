import json
import pprint

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception as e:
        print("Error:", e)
        return None

def display_student_info(student_data):
    if not student_data:
        return

    print("Student ID:", student_data["student_id"])
    print("Name:", student_data["name"])
    print("Major:", student_data["major"])
    print("GPA:", student_data["gpa"])

def main():
    data = read_json_file("student_data.json")
    if data:
        display_student_info(data)
        print("\nRaw JSON:")
        pprint.pprint(data)

if __name__ == "__main__":
    main()
