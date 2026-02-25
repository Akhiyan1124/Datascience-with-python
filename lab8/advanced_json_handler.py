import json
import os

class JSONFileError(Exception):
    pass

class JSONProcessor:

    def load_json(self, filename):
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError("File does not exist.")

            with open(filename, 'r') as file:
                data = json.load(file)

            print("JSON processed successfully.")
            return data

        except FileNotFoundError as e:
            raise JSONFileError(e)

        except json.JSONDecodeError as e:
            raise JSONFileError(f"Invalid JSON: {e}")

        except Exception as e:
            raise JSONFileError(f"Unexpected error: {e}")


if __name__ == "__main__":
    processor = JSONProcessor()
    try:
        processor.load_json("valid.json")
    except JSONFileError as e:
        print(e)
