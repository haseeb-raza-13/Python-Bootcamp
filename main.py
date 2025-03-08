from src.logging import logger
from src.exception.exception import ProjectException
import sys

from src.components.dataingestion import DataIngestion

from src.components.dataingestion import DataIngestionArtifact
from src.components.dataingestion import DataIngestionConfig


if __name__=="__main__":
    
    data_ingestion=DataIngestion()
    train_data, test_data = data_ingestion.initate_data_ingestion()
    




