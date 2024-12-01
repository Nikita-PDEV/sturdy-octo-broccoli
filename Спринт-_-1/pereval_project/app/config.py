import os  
from dotenv import load_dotenv  

load_dotenv()  # Загружаем переменные окружения из .env файла  

DATABASE_CONFIG = {  
    "host": os.getenv("FSTR_DB_HOST"),  
    "port": os.getenv("FSTR_DB_PORT"),  
    "user": os.getenv("FSTR_DB_LOGIN"),  
    "password": os.getenv("FSTR_DB_PASS"),  
    "dbname": "postgres"  
}