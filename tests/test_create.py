"""Tests retrieval of database tables with Django ORM

"""

import sys
import django
from dotenv import load_dotenv
import pytest


Run = None


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


def test_get_run():
    Run.objects.all()
    assert True


def test_get_runs():
    Run.objects.all()
    assert True
