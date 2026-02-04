import csv
import logging
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "input.csv")


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CSVReader:
    def __init__(self,filepath):
        self.filepath=filepath
    
    def read(self):
        logging.info(f'Reading the CSV File')
        try:
            with open(self.filepath,'r',newline='') as file:
                return(list(csv.reader(file)))
        except FileNotFoundError as fe:
                logging.exception(f'Error loading the file {self.filepath}')
                raise
    def log_rows(self, rows):
        logging.info("Logging CSV rows")
        for row in rows:
            logging.info(row)
            
def main():
        reader=CSVReader(DATA_PATH)
        data=reader.read()
        reader.log_rows(data)
    
if __name__=="__main__":
    main()