import sys
from yoyo import read_migrations, get_backend
import os
import logging as logger

def apply_migrations(backend, migrations):
    """
    Executes migrations
    :param backend: Yoyo Backend
    :param migrations: Yoyo migrations model
    :return: True if migrations were applied successfully, False otherwise.
    """
    try:
        logger.info(f"Backend lock")
        with backend.lock():
            logger.info(f"Running migrations")
            backend.apply_migrations(backend.to_apply(migrations))
            return True
    except Exception as e:
        logger.error(f"Error applying migrations {e}")
        return False


def init_yoyo(conn):
    """
    Builds a yoyo backend and migrations model
    :param conn: SQL Alchemy engine object
    :return: A yoyo backend and a yoyo migrations representation
    """
    # Building backend
    logger.info("Building yoyo backend")
    yoyo_backend = get_backend(conn)

    # Building migrations
    migrations_folder = './migrations' # os.environ.get("MIGRATIONS_FOLDER")
    logger.info(f"Reading migrations from {migrations_folder}")
    yoyo_migrations = read_migrations(migrations_folder)
    return yoyo_backend, yoyo_migrations


def _get_connection_info():
    """
    Gets the connection info for the database
    :return: connection info
    """
    return {
        "database": 'prueba', #os.environ["DB_NAME"],
        "host": '127.0.0.1', #os.environ["DB_HOST"],
        "port": '5432', #os.environ["DB_PORT"],
        "user": 'martinmarchetta', # os.environ["DB_USERNAME"],
        "pass": '' # os.environ["DB_PASSWORD"],
    }


def _get_connection_url():
    connection_info = _get_connection_info()
    connection_url = 'postgresql://{}:{}@{}:{}/{}'.format(
        connection_info["user"],
        connection_info["pass"],
        connection_info["host"],
        connection_info["port"],
        connection_info["database"]
        )
    return connection_url


def run_migrations():
    logger.info("Initializing DB versioning")
    logger.info("Connecting to database")
    logger.info("Initializing yoyo")
    yoyo_backend, yoyo_migrations = init_yoyo(_get_connection_url())
    logger.info("Applying migrations")
    success = apply_migrations(yoyo_backend, yoyo_migrations)
    if not success:
        logger.error("Error applying migrations")
        sys.exit(1)
    logger.info("Done!")
