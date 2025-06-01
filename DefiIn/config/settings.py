import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    INFURA_URL = os.getenv("INFURA_URL")
    ONEINCH_API_KEY = os.getenv("ONEINCH_API_KEY")
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")
    TEST_POOL = os.getenv("TEST_POOL")

settings = Settings()

"""
config/settings.py (Управление настройками)
Функционал:

Загружает переменные из .env через python-dotenv

Предоставляет централизованный доступ к настройкам через класс Settings

Ключевые методы:

python
load_dotenv()  # Инициализация переменных окружения
settings = Settings()  # Единая точка доступа к конфигам
Зачем нужен:
Упрощает модификацию настроек без изменения кода в других модулях.
"""