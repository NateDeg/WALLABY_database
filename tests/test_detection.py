"""Tests CRUD operations on wallaby.detection table.

"""

import sys
import json
import django
import pytest
from dotenv import load_dotenv
from tests.common import db_conn, run, instance, detection  # noqa


Run = None
Instance = None
Detection = None


@pytest.fixture(scope="session", autouse=True)
def django_setup():
    """Setup database connection and Django shell

    """
    load_dotenv()
    sys.path.append('./orm/')
    django.setup()
    global Run, Instance, Detection
    from orm.source_finding.models import Run, Instance, Detection
    return


def test_create_detection(db_conn):
    run_row = Run.objects.create(**run)
    assert(run_row is not None)

    instance_row = Instance.objects.create(**{**{'run_id': run_row.id}, **instance})
    assert(instance_row is not None)

    detection_row = Detection.objects.create(
        **{**{
            'run_id': run_row.id,
            'instance_id': instance_row.id
            },
            **detection
        }
    )
    assert(detection_row is not None)

    # assert entry in database exists
    query = "SELECT * FROM wallaby.detection WHERE name IN (%s)"
    db_conn.execute(query, (detection['name'],))
    res = dict(db_conn.fetchone())
    assert(detection['name'] == res['name'])


def test_delete_detection(db_conn):
    Detection.objects.filter(name=detection['name']).delete()

    # assert detection database entry does not exist
    query = "SELECT * FROM wallaby.detection WHERE name IN (%s)"
    db_conn.execute(query, (detection['name'],))
    res = db_conn.fetchone()
    assert(res is None)

    # cleanup
    Run.objects.filter(name=run['name']).delete()
    Instance.objects.filter(filename=instance['filename']).delete()
    run_query = "SELECT * FROM wallaby.run WHERE name IN (%s)"
    instance_query = "SELECT * FROM wallaby.instance WHERE filename IN (%s)"
    db_conn.execute(run_query, (run['name'],))
    res = db_conn.fetchone()
    assert(res is None)
    db_conn.execute(instance_query, (instance['filename'],))
    res = db_conn.fetchone()
    assert(res is None)

