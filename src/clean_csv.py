import csv
import logging
import json
# Load configuration from config.json
def load_config(config_file):
    with open(config_file, 'r') as config_file:
        try:
            config = json.load(config_file)
            logging.info(f"Configuration loaded successfully.")
            return config
        except FileNotFoundError:
            logging.error("config.json file not found.")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Error loading config.json: {e}")
            raise

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Reading the CSV file and printing its contents 
def read_csv(input_file='Input.csv'):
    csv_rows=[]
    try:
        with open(input_file, mode='r', newline='') as csvfile:
            logging.info ("Reading the CSV file...")     
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                csv_rows.append(row) 
    except FileNotFoundError:
        logging.error(f"The file '{input_file}' was not found.")
        raise
    return(csv_rows)

# Cleaning the CSV data by removing empty fields and rows
def clean_csv(csv_rows):
    cleaned_rows = []
    for row in csv_rows:
        cleaned_row = [field.strip() for field in row if field.strip() != '']
        if cleaned_row:
            cleaned_rows.append(cleaned_row)
    logging.info ("Cleaned the CSV file...")     
    return cleaned_rows

# Writing to a new CSV file with specified formatting
def write_csv(output_file, cleaned_rows):
    with open(output_file, mode='w', newline='') as csvfile:
        logging.info ("Writing to a new CSV file...")
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in cleaned_rows:
            csvwriter.writerow(row)
    logging.info("New CSV file created successfully.")

def main():
    #input_file = 'Input.csv'
    #output_file = 'Clean_CSV.csv'
    try:
        config_file='config.json'
        config=load_config(config_file)
        csv_rows = read_csv(config['input_file'])
        cleaned_rows = clean_csv(csv_rows)
        write_csv(config['output_file'], cleaned_rows) 
    except KeyError:
        logging.error("Configuration file is missing required keys.")
        raise
if __name__ == "__main__":
    main()  
    
# Cleaning the CSV data by removing empty fields and rows   
