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

detection = {
    'name': 'SoFiA J131553.06-183956.0',
    'access_url': 'https://wallaby.aussrc.org/wallaby/vo/dl/dlmeta?ID=6963',
    'access_format': 'application/x-votable+xml;content=datalink',
    'x': 1567.8936174614087,
    'y': 2326.2644997094926,
    'z': 3033.942501722277,
    'x_min': 449,
    'x_max': 458,
    'y_min': 189,
    'y_max': 199,
    'z_min': 1347,
    'z_max': 1377,
    'n_pix': 1299,
    'f_min': -0.003914461005479097,
    'f_max': 0.007486303802579641,
    'f_sum': 883.2340719649548,
    'rel': 0.9284305395442486,
    'rms': 0.001326740559048503,
    'w20': 502806.7732346451,
    'w50': 237456.2053702422,
    'ell_maj': 4.447757999128199,
    'ell_min': 3.694980582702955,
    'ell_pa': 7.594256154836131,
    'ell3s_maj': 5.181348233758756,
    'ell3s_min': 3.522203571729592,
    'ell3s_pa': 13.8613439869066,
    'kin_pa': 357.8773091211234,
    'ra': 198.9710627380368,
    'dec': -18.66554246188289,
    'err_x': 0.2563692589990081,
    'err_y': 0.2843866478737606,
    'err_z': 0.9542396046471767,
    'err_f_sum': 166.8667250705696,
    'freq': 1351684120.402208,
    'unresolved': False
}

source = {
    'name': 'WALLABY J131553-183956',
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
