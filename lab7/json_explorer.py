import json
import sys

def explore_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)

        print("Top Level Keys:")
        for key in data.keys():
            print("-", key)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        explore_json(sys.argv[1])
    else:
        print("Usage: python3 json_explorer.py company_data.json")
