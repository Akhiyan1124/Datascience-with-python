import csv
from collections import defaultdict

def calculate_statistics(filename):
    sales_by_rep = defaultdict(float)

    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                total = int(row['Quantity']) * float(row['Price'])
                sales_by_rep[row['Sales_Rep']] += total

        print("Sales by Representative:")
        for rep, total in sales_by_rep.items():
            print(f"{rep}: ${total:.2f}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    calculate_statistics("sales_data.csv")
