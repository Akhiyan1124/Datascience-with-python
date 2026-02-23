import csv

def read_sales_data(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                quantity = int(row['Quantity'])
                price = float(row['Price'])
                total = quantity * price

                print(f"{row['Product']} | Qty: {quantity} | Total: ${total:.2f}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    read_sales_data("sales_data.csv")
