import json

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print("JSON loaded successfully.")
            return data

    except FileNotFoundError:
        print("JSON file not found.")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    read_json_file("sample.json")
    read_json_file("missing.json")
