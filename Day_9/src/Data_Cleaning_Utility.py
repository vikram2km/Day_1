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
            logging.exception(f'File not found: {FILE_PATH}')
            raise
        except Exception as e:
            logging.exception(f'Unexpected extraction error: {e}')
            raise
        

class BaseLogger(ABC):
    @abstractmethod
    def log_rows(self,df:pd.DataFrame)->None:
        pass
class ConsoleLogger(BaseLogger):
    def log_rows(self, df:pd.DataFrame)->None:
        logging.info("Pipeline Result:")
        logging.info("\n %s",df)
    

class DataCleaner:
    @staticmethod
    def strip_spaces(df:pd.DataFrame)->pd.DataFrame:
        logging.info('Stripping whitespace from string columns')
        for col in df.select_dtypes(include="object"):
            df[col] = df[col].str.strip()
        return df
    
    @staticmethod
    def remove_duplicates(df:pd.DataFrame)->pd.DataFrame:
        logging.info("Removing duplicate rows")
        if 'id' not in df.columns:
            raise KeyError('Missing column: id')
        before = len(df)
        df=df.drop_duplicates('id')
        after = len(df)
    
        logging.info("Duplicates removed: %s", before - after)
        
        return df
    
    @staticmethod
    def fill_missing_salary(df:pd.DataFrame)->pd.DataFrame:
        logging.info('Filling Missing Salaries')
        if "salary" not in df.columns:
            raise KeyError("Missing column: salary")

        df["salary"] = df["salary"].fillna(
            df.groupby("department")["salary"].transform("mean"))

        return df
        
    @staticmethod
    def fill_missing_department(df:pd.DataFrame)->pd.DataFrame:
        logging.info('Filling missing departments')
        if 'department' in list(df.columns):   
            df['department']=df['department'].fillna('Unknown')
            return df
        else:
            logging.exception('department key is missing in the CSV file')
            raise KeyError('department key is missing in the CSV file')

class DataValidator:
    REQUIRED_COLUMNS = {"id", "salary", "department"}
    
    @staticmethod
    def validate(df:pd.DataFrame)-> bool:
        logging.info("Validating dataset")

        if not DataValidator.REQUIRED_COLUMNS.issubset(df.columns):
            raise CSVDataError("Missing required columns")

        if df["salary"].isna().any():
            raise CSVDataError("Salary still contains NULL values")

        if not df["id"].is_unique:
            raise CSVDataError("IDs are not unique")

        if (df["salary"] <= 0).any():
            raise CSVDataError("Invalid salary detected")

        logging.info("Validation passed")

        return True

class DataProfiler:
    @staticmethod
    def profile(df:pd.DataFrame)->pd.DataFrame:
        #logging.info(f"\n {df}")
        report = pd.DataFrame({
            "null_%": df.isna().mean() * 100,
            "unique_values": df.nunique()
        })
        numeric_cols = df.select_dtypes(include="number").columns

        report["min"] = None
        report["max"] = None

        report.loc[numeric_cols, "min"] = df[numeric_cols].min()
        report.loc[numeric_cols, "max"] = df[numeric_cols].max()

        duplicate_rows = df.duplicated().sum()
        
        logging.info("Duplicate rows: %s", duplicate_rows)

        for col in report[report["null_%"] > 10].index:
            logging.warning("%s has high null percentage", col)
            
        return report
    

class Pipeline:
    def __init__(self,
                 extractor:BaseExtractor,
                 cleaners:list[DataCleaner],
                 validator:type[DataValidator],
                 profiler:type[DataProfiler],
                 logger:BaseLogger)->None:
        self._extractor=extractor
        self._cleaners=cleaners
        self._validator=validator
        self._profiler=profiler       
        self._logger=logger
        
    def run(self)->None:
        try:
            data=self._extractor.extract()
            for cleaning_steps in self._cleaners:
                data=cleaning_steps(data)
            self._validator.validate(data)
            #result=data.groupby('department')['salary'].mean()
            logging.info('\n %s',data)
            profile_res = self._profiler.profile(data)
            self._logger.log_rows(profile_res) 
        except Exception as e:
            logging.exception(f'Pipeline failed: - {e}')
            raise


def main():
    csv_extractor=CSVExtractor(FILE_PATH)
    logger=ConsoleLogger()
    cleaners=[DataCleaner.strip_spaces,
              DataCleaner.remove_duplicates,
              DataCleaner.fill_missing_salary,
              DataCleaner.fill_missing_department]
    pipeline=Pipeline(csv_extractor,cleaners,DataValidator,DataProfiler,logger)
    pipeline.run()
    
if __name__=='__main__':
    main()
