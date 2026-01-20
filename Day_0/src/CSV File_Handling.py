import csv
import logging
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "input.csv")


logging.basicConfig(level=logging.INFO, format='%(asctime)s, - %(levelname)s - %(message)s')

def read_csv(filename):
    logging.info(f'Reading the CSV File {filename}')
    try:
        with open(filename,'r',newline='') as file:
            return(list(csv.reader(file)))
    except FileNotFoundError as fe:
        logging.exception(f'Error loading the file {filename}')


def print_csv(csv_file):
    logging.info('Printing the CSV File Rows')
    for row in csv_file:
        print(row)
            
def main():
        csv_file=read_csv(DATA_PATH)
        if csv_file:
            print_csv(csv_file)
    
if __name__=="__main__":
    main()