import csv

def create_summary(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.writer(outfile)

            writer.writerow(["Product", "Total Sales"])

            for row in reader:
                total = int(row['Quantity']) * float(row['Price'])
                writer.writerow([row['Product'], total])

        print("Summary file created successfully.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    create_summary("sales_data.csv", "sales_summary.csv")
