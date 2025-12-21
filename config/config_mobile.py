import os
from typing import Literal

import dotenv
import pydantic_settings

# Загружаем общие переменные окружения
dotenv.load_dotenv()


class Config(pydantic_settings.BaseSettings):
    context: Literal[
        'local_emulator', 'local_real', 'bstack'] = 'local_emulator'  # по дефолту тесты запускаются на bstack

    # Общие параметры
    DEVICE_NAME: str = 'Pixel 6'
    udid: str = ''
    timeout: float = 15.0
    remote_url: str = ''
    BROWSER_NAME: str = 'chrome'

    # BrowserStack параметры
    BROWSERSTACK_USERNAME: str = ''
    BROWSERSTACK_ACCESS_KEY: str = ''
    BROWSERSTACK_PROJECT_NAME: str = 'diplom_name'
    BROWSERSTACK_BUILD_NAME: str = 'diplom_build'
    BROWSERSTACK_SESSION_NAME: str = 'diplom_session'

    # Настройка загрузки переменных окружения
    model_config = pydantic_settings.SettingsConfigDict(
        env_file=('.env', f'.env.{os.getenv("CONTEXT", "bstack")}'),
        extra='ignore'
    )


# Создаем экземпляр конфига
config = Config()
