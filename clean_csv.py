import csv
import logging
csv_rows=[]

# Reading the CSV file and printing its contents 
logging.info ("Reading the CSV file...")     
def read_csv():
    try:
        with open('Input.csv', mode='r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                csv_rows.append(row)
        print(csv_rows)
    except FileNotFoundError:
        logging.error("The file 'Input.csv' was not found.")
        exit(1)

# Cleaning the CSV data by removing empty fields and rows
logging.info ("Cleaning the CSV file...")     
def clean_csv():
    global csv_rows
    cleaned_rows = []
    for row in csv_rows:
        cleaned_row = [field.strip() for field in row if field.strip() != '']
        if cleaned_row:
            cleaned_rows.append(cleaned_row)
    csv_rows = cleaned_rows 
    print(csv_rows)

# Writing to a new CSV file with specified formatting
logging.info ("Writing to a new CSV file...")
def write_csv():
    with open('Clean_CSV.csv', mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in csv_rows:
            csvwriter.writerow(row)
    print("New CSV file created successfully.")

def main():
    read_csv()
    clean_csv()
    write_csv() 
if __name__ == "__main__":
    main()  
    
# Cleaning the CSV data by removing empty fields and rows   
