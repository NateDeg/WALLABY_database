"""Tests CRUD operations on wallaby.tag and wallaby.tag_source_detection
tables.

"""

import sys
import django
import pytest
from dotenv import load_dotenv
from tests.common import db_conn, run, instance, detection, source  # noqa
from tests.common import tag


Run = None
Instance = None
Detection = None
Source = None
SourceDetection = None
Tag = None
TagSourceDetection = None


@pytest.fixture(scope="session", autouse=True)
def django_setup():
    """Setup database connection and Django shell

    """
    load_dotenv()
    sys.path.append('./orm/')
    django.setup()
    global Run, Instance, Detection, Source, SourceDetection
    global Tag, TagSourceDetection
    from orm.source_finding.models import Run, Instance, Detection, Source
    from orm.source_finding.models import SourceDetection, Tag, TagSourceDetection  # noqa
    return


def test_create_tag(db_conn):
    run_obj = Run.objects.create(**run)
    assert(run_obj is not None)

    instance_obj = Instance.objects.create(
        **{**{'run_id': run_obj.id}, **instance}
    )
    assert(instance_obj is not None)

    detection_obj = Detection.objects.create(**{
        **{
            'run_id': run_obj.id,
            'instance_id': instance_obj.id
        },
        **detection
    })
    assert(detection_obj is not None)

    source_obj = Source.objects.create(**source)
    assert(source_obj is not None)

    source_detection_obj = SourceDetection.objects.create(**{
        'detection_id': detection_obj.id,
        'source_id': source_obj.id
    })
    assert(source_detection_obj is not None)

    tag_obj = Tag.objects.create(**tag)
    assert(tag_obj is not None)

    tag_source_detection_obj = TagSourceDetection.objects.create(
        tag=tag_obj,
        source_detection=source_detection_obj
    )
    assert(tag_source_detection_obj is not None)

    # assert entry in database exists
    query = "SELECT * FROM wallaby.tag WHERE name IN (%s)"
    db_conn.execute(query, (tag['name'],))
    res = dict(db_conn.fetchone())
    assert(tag['name'] == res['name'])

    query = "SELECT * FROM wallaby.tag_source_detection WHERE tag_id IN (%s)"
    db_conn.execute(query, (tag_obj.id,))
    res = dict(db_conn.fetchone())
    assert(source_detection_obj.id == res['source_detection_id'])


def test_delete_source(db_conn):
    # delete tag and tag_source_detection
    tag_obj = Tag.objects.get(name=tag['name'])
    TagSourceDetection.objects.filter(tag=tag_obj).delete()
    query = "SELECT * FROM wallaby.tag_source_detection WHERE tag_id IN (%s)"
    db_conn.execute(query, (tag_obj.id,))
    res = db_conn.fetchone()
    assert(res is None)

    Tag.objects.filter(name=tag['name']).delete()
    query = "SELECT * FROM wallaby.tag WHERE name IN (%s)"
    db_conn.execute(query, (tag['name'],))
    res = db_conn.fetchone()
    assert(res is None)

    # cleanup
    source_obj = Source.objects.get(name=source['name'])
    SourceDetection.objects.filter(source=source_obj).delete()
    query = "SELECT * FROM wallaby.source_detection WHERE source_id IN (%s)"
    db_conn.execute(query, (source_obj.id,))
    res = db_conn.fetchone()
    assert(res is None)

    Source.objects.filter(name=source['name']).delete()
    query = "SELECT * FROM wallaby.source WHERE name IN (%s)"
    db_conn.execute(query, (source['name'],))
    res = db_conn.fetchone()
    assert(res is None)

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
