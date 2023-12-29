from src.CNNclassifier import logger
from src.CNNclassifier.pipeline.stage_02_preparebasemodel import PrepareBaseModelTrainingPipeline


logger.info("welcome to my channel")

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