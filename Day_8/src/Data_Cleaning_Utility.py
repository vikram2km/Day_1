import pandas as pd
import os
import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

BASE_PATH=os.path.dirname(os.path.abspath(__file__))
FILE_PATH=os.path.join(BASE_PATH,"..",'data','input_file.csv')

class CSVDataError(Exception):
    pass


class BaseExtractor(ABC):
    @abstractmethod 
    def extract(self)->pd.DataFrame:
        pass
class BaseLogger(ABC):
    @abstractmethod
    def log_rows(self,df:pd.DataFrame)->None:
        pass
  
class ConsoleLogger(BaseLogger):
    def log_rows(self, df:pd.DataFrame)->None:
        logging.info("Logging Rows")
        logging.info(df)
    
class CSVExtractor(BaseExtractor):
    def __init__(self, FilePath:str)->None:
        self._filepath=FilePath
        
    def extract(self)->pd.DataFrame:
        try:
            logging.info('Reading the CSV File')
            data=pd.read_csv(self._filepath)
            required_columns = {"id", "salary", "department"}
            if not required_columns.issubset(data.columns):
                raise CSVDataError("Missing required columns")
            return data
        except FileNotFoundError:
            logging.exception(f'Unable to fetch the file from - {FILE_PATH}')
            raise
        except Exception as e:
            logging.exception(f'Issue while extracting the file - {e}')
            raise
class DataCleaner:
    @staticmethod
    def strip_spaces(df:pd.DataFrame)->pd.DataFrame:
        logging.info('Removing leading/trailing spaces')
        return(df.apply(lambda x:x.strip() if isinstance(x,str) else x))
    @staticmethod
    def remove_duplicates(df:pd.DataFrame)->pd.DataFrame:
        logging.info('Removing Duplicates')
        if 'id' in set(df.columns):
            return (df.drop_duplicates(subset='id'))
        else:
            logging.exception('id key is missing in the CSV file')
            raise KeyError('id key is missing in the CSV file')
    @staticmethod
    def fill_missing_salary(df:pd.DataFrame)->pd.DataFrame:
        logging.info('Filling Missing Salaries')
        if 'salary' in set(df.columns):
            df.loc[:,'salary']=df['salary'].fillna(df.groupby('department')['salary'].transform('mean'))
            return df
        else:
            logging.exception('salary key is missing in the CSV file')
            raise KeyError('salary key is missing in the CSV file')
    @staticmethod
    def fill_missing_department(df:pd.DataFrame)->pd.DataFrame:
        logging.info('Filling Missing Departments')
        if 'department' in list(df.columns):   
            df.loc[:,'department']=df['department'].fillna('Unknown')
            return df
        else:
            logging.exception('department key is missing in the CSV file')
            raise KeyError('department key is missing in the CSV file')

class DataValidator:
    @staticmethod
    def validate(df:pd.DataFrame)-> int:
        logging.info('Validating the data')
        if (not df['salary'].hasnans and df['salary'].min()>0 and df['id'].is_unique):
            return True
        else:
            return False

    

class Pipeline:
    def __init__(self,
                 extractor:BaseExtractor,
                 cleaners:list[DataCleaner],
                 validator:type[DataValidator],
                 logger:BaseLogger)->None:
        self._extractor=extractor
        self._cleaners=cleaners
        self._validator=validator
        self._logger=logger
        
    def run(self)->None:
        try:
            data=self._extractor.extract()
            for cleaning_steps in self._cleaners:
                data=cleaning_steps(data)
            validation_result=self._validator.validate(data)
            if validation_result:
                logging.info('Validation Complete - Result: Valid')
                self._final_result=data.groupby('department')['salary'].mean()
                self._logger.log_rows(self._final_result) 
            else:
                raise CSVDataError('Validation Complete - Result: InValid')
        except CSVDataError:
            logging.exception('Validation Complete. Result: InValid')
            raise
        except Exception as e:
            logging.exception(f'Encountered - {e}')
            raise

def main():
    csv_extractor=CSVExtractor(FILE_PATH)
    logger=ConsoleLogger()
    cleaners=[DataCleaner.strip_spaces,
              DataCleaner.remove_duplicates,
              DataCleaner.fill_missing_salary,
              DataCleaner.fill_missing_department]
    pipeline=Pipeline(csv_extractor,cleaners,DataValidator,logger)
    pipeline.run()
    
if __name__=='__main__':
    main()
