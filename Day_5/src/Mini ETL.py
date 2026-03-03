import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class BaseExtractor(ABC):
    @abstractmethod
    def extract(self):
        pass
class BaseTransformer(ABC):
    @abstractmethod
    def transform(self, data: list[int]) -> list[int]:
        pass   
class BaseLogger(ABC):
    @abstractmethod
    def log_rows(self,rows):
        pass
        
    
class Pipeline:
    def __init__(self,extractor,transformer,logger):
        self._extractor=extractor
        self._transformer=transformer
        self._logger=logger
        
    def run(self):
        extracted_data=self._extractor.extract()
        transformed_data=self._transformer.transform(extracted_data)
        self._logger.log_rows(transformed_data)

        
        
#Composition
class ListExtractor(BaseExtractor):
    def extract(self):
        logging.info("Retrieving the Data")
        return [1,2,3,4,5,5,3,4,2,6,7,2,8,9,10]

class RemoveDuplicatesTransformer(BaseTransformer):
    def transform(self, data):
        logging.info("Transforming the Data: Getting Unique Rows")
        transformed_data=list(dict.fromkeys(data))
        return transformed_data
class MultiplyByTwoTransformer(BaseTransformer):
    def transform(self, data):
        logging.info("Transforming the Data: Multiplying By 2")
        transformed_data=[i*2 for i in data]
        return transformed_data
    
class ConsoleLogger(BaseLogger):
    def log_rows(self, rows):
        logging.info("Logging Rows")
        for row in rows:
            logging.info(row)
            
def main():
    logger=ConsoleLogger()
    extractor=ListExtractor()
    transformer=RemoveDuplicatesTransformer()
        
    pipeline=Pipeline(extractor,transformer,logger)
    pipeline.run()
    
if __name__=="__main__":
    main()