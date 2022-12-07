from django.db import models
from django.db.models import DecimalField
from orm.source_finding.models import Source


def PostgresDecimalField(*args, **kwargs):
    return DecimalField(max_digits=65535, decimal_places=12, *args, **kwargs)


class KinematicModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    source = models.ForeignKey(Source, db_column='name', to_field='name', on_delete=models.DO_NOTHING)
    ra = PostgresDecimalField()
    dec = PostgresDecimalField()
    freq = PostgresDecimalField()
    team_release = models.CharField(max_length=64)
    team_release_kin = models.CharField(max_length=64)
    vsys_model = PostgresDecimalField()
    e_vsys_model = PostgresDecimalField()
    x_model = PostgresDecimalField()
    e_x_model = PostgresDecimalField()
    y_model = PostgresDecimalField()
    e_y_model = PostgresDecimalField()
    ra_model = PostgresDecimalField()
    e_ra_model = PostgresDecimalField()
    dec_model = PostgresDecimalField()
    e_dec_model = PostgresDecimalField()
    inc_model = PostgresDecimalField()
    e_inc_model = PostgresDecimalField()
    pa_model = PostgresDecimalField()
    e_pa_model = PostgresDecimalField()
    pa_model_g = PostgresDecimalField()
    e_pa_model_g = PostgresDecimalField()
    qflag_model = models.IntegerField()
    rad = models.CharField(max_length=256)
    vrot_model = models.CharField(max_length=256)
    e_vrot_model = models.CharField(max_length=256)
    e_vrot_model_inc = models.CharField(max_length=256)
    rad_sd = models.CharField(max_length=256)
    sd_model = models.CharField(max_length=256)
    sd_fo_model = models.CharField(max_length=256)
    e_sd_model = models.CharField(max_length=256)
    e_sd_fo_model_inc = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'kinematic_model'


class WKAPPProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    kinematic_model_id = models.ForeignKey(KinematicModel, models.DO_NOTHING)
    baroloinput = models.BinaryField(blank=True, null=True)
    barolomod = models.BinaryField(blank=True, null=True)
    barolosurfdens = models.BinaryField(blank=True, null=True)
    diagnosticplot = models.BinaryField(blank=True, null=True)
    diffcube = models.BinaryField(blank=True, null=True)
    fatinput = models.BinaryField(blank=True, null=True)
    fatmod = models.BinaryField(blank=True, null=True)
    fullresmodelcube = models.BinaryField(blank=True, null=True)
    fullresproccube = models.BinaryField(blank=True, null=True)
    modcube = models.BinaryField(blank=True, null=True)
    procdata = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wkapp_product'
