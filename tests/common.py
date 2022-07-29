"""Data for tests

"""

import os
import json
import pytest
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv


run = {
    'name': 'test',
    'sanity_thresholds': json.dumps({'test': 'test'})
}

instance = {
    'filename': 'hydra',
    'boundary': {0},
    'run_date': '2021-11-16 05:22:03.544337',
    'parameters': json.dumps({'test': 'test'})
}


@pytest.fixture
def db_conn():
    load_dotenv()
    conn = psycopg2.connect(
        dbname=os.environ['DATABASE_NAME'],
        host=os.environ['DATABASE_HOST'],
        user=os.environ['DATABASE_USER'],
        password=os.environ['DATABASE_PASS'],
        port=os.getenv('DATABASE_PORT', 5432)
    )
    conn.autocommit = True
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    yield cursor
    cursor.close()
    conn.close()
