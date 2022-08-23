"""Tests CRUD operations on wallaby.kinematic_model table.

"""

import sys
import json
import django
import pytest
from dotenv import load_dotenv
from tests.common import db_conn, run  # noqa


KinematicModel = None


@pytest.fixture(scope="session", autouse=True)
def django_setup():
    """Setup database connection and Django shell

    """
    load_dotenv()
    sys.path.append('./orm/')
    django.setup()
    global KinematicModel
    from orm.kinematic_model.models import KinematicModel
    return


def test_read_kinematic_model(db_conn):
    row = KinematicModel.objects.get(id=1)
    assert(row is not None)
