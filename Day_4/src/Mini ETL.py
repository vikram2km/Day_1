import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataSource:
    def get_data(self):
        return [1,2,3,4,5,5,3,4,2,6,7,2,8,9,10]
    
class Pipeline:
    def __init__(self,extractor,transformer,logger):
        self._extractor=extractor
        self._transformer=transformer
        self._logger=logger
        
    def run(self,datasource):
        extracted_data=self._extractor.extract(datasource)
        transformed_data=self._transformer.transform(extracted_data)
        self._logger.log_rows(transformed_data)

        
        
#Composition
class Extractor:
    def extract(self, datasource):
        logging.info("Retriving the Data")
        return datasource.get_data()

class Transformer:
    def transform(self, data):
        logging.info("Transforming the Data")
        transformed_data=list(dict.fromkeys(data))
        return transformed_data
    
class Logger:
    def log_rows(self, rows):
        logging.info("Logging Unique rows")
        for row in rows:
            logging.info(row)
            
def main():
    logger=Logger()
    extractor=Extractor()
    transformer=Transformer()
    source=DataSource()
        
    pipeline=Pipeline(extractor,transformer,logger)
    pipeline.run(source)
    
if __name__=="__main__":
    main()