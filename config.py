import os

from dotenv import dotenv_values

env_values = {
    **dotenv_values(".env"),
    **os.environ,
}


class DBConfig:
    host = env_values.get('PG_HOST')
    port = env_values.get('PG_PORT')
    username = env_values.get('PG_USERNAME')
    password = env_values.get('PG_PASSWORD')
    db_name = env_values.get('PG_DBNAME')
    db_url = env_values.get('PG_DBURL')


class AppConfig:
    title = env_values.get('APP_TITLE')
    docs_url = env_values.get('APP_DOCS_URL')
    redoc_url = env_values.get('APP_REDOC_URL')


db_config = DBConfig()
app_config = AppConfig()
