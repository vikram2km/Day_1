import csv
import logging
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "input.csv")


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#Composition
class Logger:
    def log_rows(self, rows):
        logging.info("Logging CSV rows")
        for row in rows:
            logging.info(row)

class Validator:
    def validate(self,data):
        logging.info ("Validating & Cleaning the CSV file...")
        cleaned_rows = []
        if data:
            for row in data:
                cleaned_rows.append([field.strip() for field in row if field.strip() != ''])
                cleaned_rows=[row for row in cleaned_rows if len(row)>0]
            return cleaned_rows
        else:
            raise ValueError('The CSV file is Empty')
        
class CSVReader:
    def __init__(self,filepath):
        self._filepath=filepath
    
    def read(self):
        logging.info('Reading the CSV File...')
        try:
            with open(self._filepath,'r',newline='') as file:
                return(list(csv.reader(file)))
        except FileNotFoundError as fe:
            logging.exception(f'Error loading the file {self._filepath}')
            raise

class Pipeline:
    def __init__(self, reader, validator, logger):
        self._reader = reader
        self._validator = validator
        self._logger = logger

    def run(self):
        data = self._reader.read()
        validated = self._validator.validate(data)
        self._logger.log_rows(validated)


def main():
        filelogger=Logger()
        reader=CSVReader(DATA_PATH)
        validator=Validator()
        
        pipeline = Pipeline(reader, validator, filelogger)
        pipeline.run()

if __name__=="__main__":
    main()