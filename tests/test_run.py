"""Tests CRUD operations on wallaby.run table.

"""

import sys
import json
import django
import pytest
from dotenv import load_dotenv
from tests.common import db_conn, run  # noqa


Run = None


@pytest.fixture(scope="session", autouse=True)
def django_setup():
    """Setup database connection and Django shell

    """
    load_dotenv()
    sys.path.append('./orm/')
    django.setup()
    global Run
    from orm.source_finding.models import Run
    return


def test_create_run(db_conn):
    row = Run.objects.create(**run)
    assert(row is not None)

    # assert entry in database exists
    query = "SELECT * FROM wallaby.run WHERE name IN (%s)"
    db_conn.execute(query, (run['name'],))
    res = dict(db_conn.fetchone())
    assert(run.items() <= res.items())


def test_read_run(db_conn):
    row = Run.objects.get(name=run['name'])
    assert(row is not None)


def test_update_run(db_conn):
    update = json.dumps({'test': 'new_value'})
    row = Run.objects.get(name=run['name'])
    row.sanity_thresholds = update
    row.save()

    # assert content in database
    query = "SELECT * FROM wallaby.run WHERE name IN (%s)"
    db_conn.execute(query, (run['name'],))
    res = dict(db_conn.fetchone())
    assert(res['sanity_thresholds'] == update)


def test_delete_run(db_conn):
    Run.objects.filter(name=run['name']).delete()

    # assert database entry does not exist
    query = "SELECT * FROM wallaby.run WHERE name IN (%s)"
    db_conn.execute(query, (run['name'],))
    res = db_conn.fetchone()
    assert(res is None)
