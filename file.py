import os

folders = [
    "app/api/v1",
    "app/core",
    "app/models",
    "app/schemas",
    "app/repositories",
    "app/services",
    "app/storage",
    "app/middleware",
    "app/utils",
    "tests",
    "migrations",
    "uploads",
    "logs"
]

files = {
    "app/__init__.py": "",
    "app/main.py": "",
    
    "app/api/__init__.py": "",
    "app/api/v1/__init__.py": "",
    "app/api/v1/auth.py": "",
    "app/api/v1/users.py": "",
    "app/api/v1/documents.py": "",
    "app/api/v1/folders.py": "",
    "app/api/v1/permissions.py": "",
    "app/api/v1/audit.py": "",

    "app/core/__init__.py": "",

    "app/core/config.py": """
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME:str = "DMS"
    DATABASE_URL:str = ""

    class Config:
        env_file = ".env"

settings = Settings()
""",

    "app/core/database.py": """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = ""

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
""",

    "app/core/security.py": "",

    "app/utils/logger.py": '''
import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(
    LOG_DIR,
    f"dms_{datetime.now().strftime('%Y%m%d')}.log"
)

logger = logging.getLogger("dms")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(filename)s | %(funcName)s | %(message)s"
)

file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=5*1024*1024,
    backupCount=5
)

file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)
''',

    "app/utils/exception.py": '''
import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    return (
        f"Error occurred in script [{file_name}] "
        f"line [{exc_tb.tb_lineno}] "
        f"error [{str(error)}]"
    )

class CustomException(Exception):

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message,
            error_detail
        )

    def __str__(self):
        return self.error_message
''',

    "app/models/__init__.py": "",
    "app/models/user.py": "",
    "app/models/document.py": "",
    "app/models/folder.py": "",
    "app/models/permission.py": "",
    "app/models/audit_log.py": "",

    "app/schemas/__init__.py": "",
    "app/schemas/user.py": "",
    "app/schemas/document.py": "",
    "app/schemas/folder.py": "",
    "app/schemas/auth.py": "",

    "app/repositories/__init__.py": "",
    "app/repositories/user_repository.py": "",
    "app/repositories/document_repository.py": "",
    "app/repositories/folder_repository.py": "",

    "app/services/__init__.py": "",
    "app/services/auth_service.py": "",
    "app/services/document_service.py": "",
    "app/services/folder_service.py": "",
    "app/services/search_service.py": "",

    "app/storage/__init__.py": "",
    "app/storage/local_storage.py": "",
    "app/storage/s3_storage.py": "",
    "app/storage/azure_storage.py": "",

    "app/middleware/__init__.py": "",
    "app/middleware/auth.py": "",
    "app/middleware/request_logger.py": "",

    ".env": "",

    "requirements.txt": """
fastapi
uvicorn
sqlalchemy
pydantic
pydantic-settings
python-dotenv
alembic
psycopg2-binary
""",

    "setup.py": '''
from setuptools import setup, find_packages

setup(
    name="dms",
    version="0.0.1",
    author="Your Name",
    packages=find_packages(),
    install_requires=[]
)
'''
}


def create_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    for file_path, content in files.items():
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    print("DMS Boilerplate Generated Successfully")


if __name__ == "__main__":
    create_structure()