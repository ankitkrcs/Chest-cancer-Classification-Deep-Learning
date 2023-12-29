from src.CNNclassifier import logger
from src.CNNclassifier.pipeline.stage_02_preparebasemodel import PrepareBaseModelTrainingPipeline
from src.CNNclassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.CNNclassifier.pipeline.stage_03_modeltraining import ModelTrainingPipeline
logger.info("welcome to my channel")


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"*********************")
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"*********************")
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"
try:
    logger.info(f"*********************")
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<<<")
    training_model= ModelTrainingPipeline()
    training_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e