"""Tests retrieval of database tables with Django ORM

"""

import sys
import json
import django
import random
from dotenv import load_dotenv
import pytest


Run = None
RUN_NAME = 'test_run'


@pytest.fixture(scope="session", autouse=True)
def db_conn():
    """Setup database connection and Django shell

    """
    load_dotenv()
    sys.path.append('./orm/')
    django.setup()
    global Run
    from orm.source_finding.models import Run
    return


def test_create_run():
    run = Run.objects.create(
        name=RUN_NAME,
        sanity_thresholds=json.dumps({'test': 'test'})
    )
    assert(run is not None)


def test_delete_run():
    Run.objects.filter(name=RUN_NAME).delete()
