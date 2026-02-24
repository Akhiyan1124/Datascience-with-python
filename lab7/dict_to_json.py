import json
from datetime import datetime

library_data = {
    "library_name": "Central University Library",
    "established": 1965,
    "total_books": 150000,
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# Convert dictionary to JSON string
json_string = json.dumps(library_data, indent=4)
print("JSON String:")
print(json_string)

# Write to file
with open("library_data.json", "w") as file:
    json.dump(library_data, file, indent=4)

print("library_data.json created successfully.")
