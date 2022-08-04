"""Test that a user will be able to retrieve metadata from a source.

    Use source WALLABY J131858-150054 from NGC 5044 DR2

"""

import sys
import json
import django
import pytest
from dotenv import load_dotenv
from tests.common import db_conn, source  # noqa


SOURCE_NAME = 'WALLABY J131858-150054'
Run = None
Instance = None
Detection = None
Source = None
SourceDetection = None
Observation = None
ObservationMetadata = None
Tile = None
Postprocessing = None


@pytest.fixture(scope="session", autouse=True)
def django_setup():
    """Setup database connection and Django shell

    """
    load_dotenv(dotenv_path='./tests/.env.prod')
    sys.path.append('./orm/')
    django.setup()
    global Run, Instance, Detection, Source, SourceDetection
    global Observation, ObservationMetadata, Tile, Postprocessing
    from orm.source_finding.models import Run, Instance, Detection, Source, SourceDetection
    from orm.operations.models import Observation, ObservationMetadata, Tile, Postprocessing
    return


def test_retrieve_observation_metadata_for_source():
    """Get observation metadata for a source.

    """
    source_obj = Source.objects.get(name=SOURCE_NAME)
    assert (source_obj is not None)

    source_detection_obj = SourceDetection.objects.get(source=source_obj)
    assert (source_detection_obj is not None)

    detection_obj = Detection.objects.get(id=source_detection_obj.detection_id)
    assert (detection_obj is not None)

    run_obj = Run.objects.get(id=detection_obj.run_id)
    assert (run_obj is not None)

    postprocessing_obj = Postprocessing.objects.get(run_id=run_obj.id)
    assert (postprocessing_obj is not None)

    tile_obj = Tile.objects.get(identifier=postprocessing_obj.name)
    assert (tile_obj is not None)

    obs_A = Observation.objects.get(id=tile_obj.footprint_A.id)
    assert (obs_A is not None)
    obs_B = Observation.objects.get(id=tile_obj.footprint_B.id)
    assert (obs_B is not None)

    obs_meta_A = ObservationMetadata.objects.get(observation=obs_A)
    assert (obs_meta_A is not None)
    obs_meta_B = ObservationMetadata.objects.get(observation=obs_B)
    assert (obs_meta_B is not None)

    print(obs_meta_A.__dict__)
    print(obs_meta_B.__dict__)
