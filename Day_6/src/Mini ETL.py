import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PipelineDataError(Exception):
    pass

class BaseExtractor(ABC):
    @abstractmethod
    def extract(self)->list[int]:
        pass
class BaseTransformer(ABC):
    @abstractmethod
    def transform(self, data: list[int]) -> list[int]:
        pass   
class BaseLogger(ABC):
    @abstractmethod
    def log_rows(self,rows:list[int])->None:
        pass
        
    
class Pipeline:
    def __init__(self,
                 extractor:BaseExtractor,
                 transformers:list[BaseTransformer],
                 logger:BaseLogger)->None:
        self._extractor=extractor
        self._transformers=transformers
        self._logger=logger
        
    def run(self)->None:
        data=self._extractor.extract()
        if data is None:
            raise PipelineDataError("Extractor returned None")
        if not data:
            logging.warning("Extractor returned empty data")
            return
        for transformer in self._transformers:
            data=transformer.transform(data)
            if data is None:
                raise PipelineDataError("Transformer returned None")
            if not data:
                logging.warning(f"{transformer.__class__.__name__} returned empty data")
        self._logger.log_rows(data)            
        
#Composition
class ListExtractor(BaseExtractor):
    def extract(self):
        logging.info("Extracting Data")
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
    
class FilterEvenNumbersTransformer(BaseTransformer):
    def transform(self, data):
        logging.info("Transforming the Data: Filtering Even Numbers")
        transformed_data=[i for i in data if i%2==0]
        return transformed_data
    
class ConsoleLogger(BaseLogger):
    def log_rows(self, rows):
        logging.info("Logging Rows")
        for row in rows:
            logging.info(row)
            
def main():
    logger=ConsoleLogger()
    extractor=ListExtractor()
    transformers=[RemoveDuplicatesTransformer(),FilterEvenNumbersTransformer(),MultiplyByTwoTransformer()]
    pipeline=Pipeline(extractor,transformers,logger)
    pipeline.run()
    
if __name__=="__main__":
    main()