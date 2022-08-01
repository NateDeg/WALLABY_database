"""Tests CRUD operations on wallaby.source and wallaby.source_detection tables.

"""

import sys
import django
import pytest
from dotenv import load_dotenv
from tests.common import db_conn, run, instance, detection, source  # noqa


Run = None
Instance = None
Detection = None
Source = None
SourceDetection = None


@pytest.fixture(scope="session", autouse=True)
def django_setup():
    """Setup database connection and Django shell

    """
    load_dotenv()
    sys.path.append('./orm/')
    django.setup()
    global Run, Instance, Detection, Source, SourceDetection
    from orm.source_finding.models import Run, Instance, Detection, Source
    from orm.source_finding.models import SourceDetection
    return


def test_create_source(db_conn):
    run_row = Run.objects.create(**run)
    assert(run_row is not None)

    instance_row = Instance.objects.create(
        **{**{'run_id': run_row.id}, **instance}
    )
    assert(instance_row is not None)

    detection_row = Detection.objects.create(**{
        **{
            'run_id': run_row.id,
            'instance_id': instance_row.id
        },
        **detection
    })
    assert(detection_row is not None)

    source_row = Source.objects.create(**source)
    assert(source_row is not None)

    source_detection_row = SourceDetection.objects.create(**{
        'detection_id': detection_row.id,
        'source_id': source_row.id
    })
    assert(source_detection_row is not None)

    # assert entry in database exists
    query = "SELECT * FROM wallaby.source WHERE name IN (%s)"
    db_conn.execute(query, (source['name'],))
    res = dict(db_conn.fetchone())
    assert(source['name'] == res['name'])

    query = "SELECT * FROM wallaby.source_detection WHERE source_id IN (%s)"
    db_conn.execute(query, (source_row.id,))
    res = dict(db_conn.fetchone())
    assert(source_row.id == res['source_id'])
    assert(detection_row.id == res['detection_id'])


def test_delete_source(db_conn):
    # delete source_detection
    source_obj = Source.objects.get(name=source['name'])
    SourceDetection.objects.filter(source=source_obj).delete()
    query = "SELECT * FROM wallaby.source_detection WHERE source_id IN (%s)"
    db_conn.execute(query, (source_obj.id,))
    res = db_conn.fetchone()
    assert(res is None)

    # delete source
    Source.objects.filter(name=source['name']).delete()
    query = "SELECT * FROM wallaby.source WHERE name IN (%s)"
    db_conn.execute(query, (source['name'],))
    res = db_conn.fetchone()
    assert(res is None)

    # cleanup
    Detection.objects.filter(name=detection['name']).delete()
    detection_query = "SELECT * FROM wallaby.detection WHERE name IN (%s)"
    db_conn.execute(detection_query, (detection['name'],))
    res = db_conn.fetchone()
    assert(res is None)

    Instance.objects.filter(filename=instance['filename']).delete()
    instance_query = "SELECT * FROM wallaby.instance WHERE filename IN (%s)"
    db_conn.execute(instance_query, (instance['filename'],))
    res = db_conn.fetchone()
    assert(res is None)

    Run.objects.filter(name=run['name']).delete()
    run_query = "SELECT * FROM wallaby.run WHERE name IN (%s)"
    db_conn.execute(run_query, (run['name'],))
    res = db_conn.fetchone()
    assert(res is None)
