from textsummarizer.logging import logger
from textsummarizer.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from textsummarizer.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline,
)
from textsummarizer.pipeline.stage_03_data_transformation import (
    DataTransformationTrainPipeline,
)
from textsummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started <<<<<")
    data_validation = DataTransformationTrainPipeline()
    data_validation.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started <<<<<")
    data_validation = ModelTrainerPipeline()
    data_validation.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e
