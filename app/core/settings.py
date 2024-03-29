import os
from pydantic import BaseSettings
from starlette.config import Config


config = Config("app/environment/environment.env")
class Settings(BaseSettings):
    environment: str = os.getenv("BULD_ENVIRONMENT", "dev")
    DEVICE = config("device", default='')
    CHECKPOINT_PATH = config("checkpoint_path", default="")
    MAT_PATH = config("mat_path", default="")
    MODEL_PATH = config("model_path", default="")
    RESULT_PATH = config("result_path", default="")
    RESNET18_MODEL = config("resnet18_model", default="")
    RESNET18_MODEL_PY26 = config("resnet18_model_py26", default="")
    CONTEXT_MODEL = BODY_MODEL = config("context_model",default="")
    WHISPER_MODEL_PATH_NAME = config("whisper_model_name", default="")
    
    ID_MAT =config("id_mat", default="")
    ID_MODEL = config("id_model", default="")
    ID_RESNET18 = config("id_resnet18", default="")
    ID_RESNET18_PY26 = config("id_resnet18_py36", default="")
    ID_WHISPER_CHECKPOINT = config("id_whisper_checkpoint", default="")                    
    TEMP_PATH = config("temp_path", default="")
    SCR_FOLDER_NAME = config("scr_folder_name", default="")

    ID_FACENET_MODEL = config("id_facenet_model", default="")
    ID_DLIB_MODEL = config("id_dlib_model", default="")
    ID_EMOTION_MODEL = config("id_emotion_model", default="")
    ID_AGE_MODEL = config("id_age_model", default="")
    ID_GENDER_MODEL = config("id_gender_model", default="")
    ID_RACE_MODEL = config("id_race_model", default="")
    DETECTOR_BACKEND_NAME = config("detector_backend_name", default="")
    DECTECOR_MODEL_CHECKPOINT_NAME= config("detector_backend_checkpoint_path_name", default="")
    FACE_ANALYST_MODEL_NAME = config("face_analyst_model_name", default="")
    FACE_ANALYST_MODEL_CHECKPOINT_PATH_NAME = config("face_analyst_model_checkpoint_path_name", default="")
    EMOTION_CHECKPOINT_PATH_NAME = config("emotion_checkpoint_path_name", default="")
    EMOTION_MODEL_NAME = config("emotion_model_name", default="")
    AGE_CHECKPOINT_PATH_NAME = config("age_checkpoint_path_name", default="")
    AGE_MODEL_NAME = config("age_model_name", default="")
    GENDER_CHECKPOINT_PATH_NAME = config("gender_checkpoint_path_name", default="")
    GENDER_MODEL_NAME = config("gender_model_name", default="")
    RACE_CHECKPOINT_PATH_NAME = config("race_checkpoint_path_name", default="")
    RACE_MODEL_NAME = config("race_model_name", default="")
    DATABASE_IMAGE_PATH = config("database_image_path", default="")
    DEEPFACE_DISTANCE = config("deepface_distance", default="")

def get_settings():
    settings = Settings()
    return settings