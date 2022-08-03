from django.db import models
from django.db.models import DecimalField
from orm.source_finding.models import Run


def PostgresDecimalField(*args, **kwargs):
    return DecimalField(max_digits=65535, decimal_places=12, *args, **kwargs)


class Observation(models.Model):
    id = models.BigAutoField(primary_key=True)
    ra = PostgresDecimalField()
    dec = PostgresDecimalField()
    description = models.CharField(max_length=512, blank=True, null=True)
    phase = models.CharField(max_length=256, blank=True, null=True)
    image_cube_file = models.CharField(max_length=512, blank=True, null=True)
    weights_cube_file = models.CharField(max_length=512, blank=True, null=True)
    quality = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'observation'


class ObservationMetadata(models.Model):
    id = models.BigAutoField(primary_key=True)
    observation = models.ForeignKey(Observation, models.DO_NOTHING)
    parameters = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'observation_metadata'


class Tile(models.Model):
    id = models.BigAutoField(primary_key=True)
    ra = PostgresDecimalField()
    dec = PostgresDecimalField()
    identifier = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    phase = models.CharField(max_length=512, blank=True, null=True)
    footprint_A = models.ForeignKey(Observation, db_column='footprint_A', blank=True, null=True, on_delete=models.DO_NOTHING)
    footprint_B = models.ForeignKey(Observation, db_column='footprint_B', blank=True, null=True, on_delete=models.DO_NOTHING)
    image_cube_file = models.CharField(max_length=512, blank=True, null=True)
    weights_cube_file = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tile'


class Postprocessing(models.Model):
    id = models.BigAutoField(primary_key=True)
    run = models.ForeignKey(Run, models.DO_NOTHING)
    name = models.CharField(max_length=512)
    region = models.CharField(max_length=256, blank=True, null=True)
    sofia_parameter_file = models.CharField(max_length=512, blank=True, null=True)
    s2p_setup = models.CharField(max_length=512, blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'postprocessing'
