import json

def load_json(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception as e:
        print("Error:", e)
        return None

def analyze_company(data):
    company = data["company"]
    print("Company:", company["name"])
    print("Founded:", company["founded"])

    engineering = company["departments"]["engineering"]
    print("Engineering Head:", engineering["head"])

    revenue = company["financial"]["revenue"]
    growth = ((revenue["2023"] - revenue["2022"]) / revenue["2022"]) * 100
    print("Growth 2022-2023:", round(growth,2), "%")

def main():
    data = load_json("company_data.json")
    if data:
        analyze_company(data)

if __name__ == "__main__":
    main()
