"""Tests CRUD operations on wallaby.instance table.

"""

import sys
import json
import django
import pytest
from dotenv import load_dotenv
from tests.common import db_conn, run, instance  # noqa


Run = None
Instance = None


@pytest.fixture(scope="session", autouse=True)
def django_setup():
    """Setup database connection and Django shell

    """
    load_dotenv()
    sys.path.append('./orm/')
    django.setup()
    global Run, Instance
    from orm.source_finding.models import Run, Instance
    return


def test_create_instance(db_conn):
    row = Run.objects.create(**run)
    assert(row is not None)

    row = Instance.objects.create(**{**{'run_id': row.id}, **instance})
    assert(row is not None)

    # assert entry in database exists
    query = "SELECT * FROM wallaby.instance WHERE filename IN (%s)"
    db_conn.execute(query, (instance['filename'],))
    res = dict(db_conn.fetchone())
    assert(instance['filename'] == res['filename'])
    assert(instance['parameters'] == res['parameters'])


def test_read_instance(db_conn):
    row = Instance.objects.get(filename=instance['filename'])
    assert(row is not None)


def test_update_instance(db_conn):
    update = json.dumps({'test': 'new_value'})
    row = Instance.objects.get(filename=instance['filename'])
    row.parameters = update
    row.boundary = {1}  # TODO(austin): issues with boundary field
    row.save()

    # assert content in database
    query = "SELECT * FROM wallaby.instance WHERE filename IN (%s)"
    db_conn.execute(query, (instance['filename'],))
    res = dict(db_conn.fetchone())
    assert(res['parameters'] == update)


def test_delete_instance(db_conn):
    Instance.objects.filter(filename=instance['filename']).delete()

    # assert instance database entry does not exist
    query = "SELECT * FROM wallaby.instance WHERE filename IN (%s)"
    db_conn.execute(query, (instance['filename'],))
    res = db_conn.fetchone()
    assert(res is None)

    # cleanup
    Run.objects.filter(name=run['name']).delete()
    query = "SELECT * FROM wallaby.run WHERE name IN (%s)"
    db_conn.execute(query, (run['name'],))
    res = db_conn.fetchone()
    assert(res is None)
