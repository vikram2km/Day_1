import logging
import json
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Load configuration from config.json
def load_config(config_file):
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
            logging.info(f"Configuration loaded successfully.")
            return config
    except FileNotFoundError:
            logging.error("config.json file not found.")
            raise
    except json.JSONDecodeError as e:
            logging.error(f"Error loading config.json: {e}")
            raise

# Reading the CSV file and printing its contents 
def read_csv(input_file):
    try:
        logging.info ("Reading the CSV file...")     
        csv_file=pd.read_csv(input_file)
    except FileNotFoundError:
        logging.error(f"The file '{input_file}' was not found.")
        raise
    return(csv_file)

# Cleaning the CSV data by removing empty fields and rows
def clean_csv(csv_file):
    logging.info ("Cleaning the CSV file...")     
    csv_file = csv_file.dropna(axis=0, how='all')
    cleaned_rows=csv_file.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return cleaned_rows

# Writing to a new CSV file with specified formatting
def write_csv(output_file, cleaned_rows):
    cleaned_rows.to_csv(output_file, index=False)
    logging.info("New CSV file created successfully.")

def main():
    #input_file = 'Input.csv'
    #output_file = 'Clean_CSV.csv'
    try:
        config=load_config('config.json')
        required_keys = ['input_file', 'output_file']
        for key in required_keys:
            if key not in config:
                raise KeyError(f"Missing required configuration key: {key}")

        csv_file = read_csv(config['input_file'])
        cleaned_rows = clean_csv(csv_file)
        write_csv(config['output_file'], cleaned_rows) 

    except Exception as e:
        logging.exception(f"ETL job failed: {e}")
        
if __name__ == "__main__":
    main()  
  

#reading the CSV file and wirign the rows to it
 
