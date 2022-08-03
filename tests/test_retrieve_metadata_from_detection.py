"""Test that a user will be able to retrieve metadata from a source.

    Use NGC5044 Tile 1 source as a starting point.
    Will have to make sure the sequence of foreign key relationships from
    the source table to the observation_meta table exist using the ORM.

"""

import sys
import json
import django
import pytest
from dotenv import load_dotenv
from tests.common import db_conn, source  # noqa


SOURCE_NAME = 'WALLABY J134749-221757'
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
    load_dotenv()
    sys.path.append('./orm/')
    django.setup()
    global Run, Instance, Detection, Source, SourceDetection
    global Observation, ObservationMetadata, Tile, Postprocessing
    from orm.source_finding.models import Run, Instance, Detection
    from orm.source_finding.models import Source, SourceDetection
    from orm.operations.models import Observation, ObservationMetadata
    from orm.operations.models import Tile, Postprocessing
    return


def test_pass():
    pass
