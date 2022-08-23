from django.db import models
from django.db.models import DecimalField

from orm.source_finding.models import Source


def PostgresDecimalField(*args, **kwargs):
    return DecimalField(max_digits=65535, decimal_places=12, *args, **kwargs)


class KinematicModel(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    name = models.ForeignKey(Source, db_column='Name', to_field='name', on_delete=models.DO_NOTHING)
    ra = PostgresDecimalField(db_column='RA')
    dec = PostgresDecimalField(db_column='DEC')
    freq = PostgresDecimalField()
    team_release = models.CharField(max_length=64)
    team_release_kin = models.CharField(max_length=64)
    Vsys_model = PostgresDecimalField()
    e_Vsys_model = PostgresDecimalField()
    X_model = PostgresDecimalField()
    e_X_model = PostgresDecimalField()
    Y_model = PostgresDecimalField()
    e_Y_model = PostgresDecimalField()
    RA_model = PostgresDecimalField()
    e_RA_model = PostgresDecimalField()
    DEC_model = PostgresDecimalField()
    e_DEC_model = PostgresDecimalField()
    Inc_model = PostgresDecimalField()
    e_Inc_model = PostgresDecimalField()
    PA_model = PostgresDecimalField()
    e_PA_model = PostgresDecimalField()
    PA_model_g = PostgresDecimalField()
    e_PA_model_g = PostgresDecimalField()
    QFlag_model = models.IntegerField()
    Rad = models.CharField(max_length=256)
    Vrot_model = models.CharField(max_length=256)
    e_Vrot_model = models.CharField(max_length=256)
    e_Vrot_model_inc = models.CharField(max_length=256)
    Rad_SD = models.CharField(max_length=256)
    SD_model = models.CharField(max_length=256)
    SD_FO_model = models.CharField(max_length=256)
    e_SD_model = models.CharField(max_length=256)
    e_SD_FO_model_inc = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'kinematic_model'
