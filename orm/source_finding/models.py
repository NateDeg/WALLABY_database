from django.db import models
from django.db.models import DecimalField


def PostgresDecimalField(*args, **kwargs):
    return DecimalField(max_digits=65535, decimal_places=12, *args, **kwargs)


class Run(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    sanity_thresholds = models.JSONField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        db_table = 'run'
        unique_together = (('name', 'sanity_thresholds'),)


class Instance(models.Model):
    id = models.BigAutoField(primary_key=True)
    run = models.ForeignKey(Run, models.DO_NOTHING)
    filename = models.TextField()
    boundary = models.TextField()
    run_date = models.DateTimeField()
    flag_log = models.BinaryField(blank=True, null=True)
    reliability_plot = models.BinaryField(blank=True, null=True)
    log = models.BinaryField(blank=True, null=True)
    parameters = models.JSONField()
    version = models.CharField(max_length=512, blank=True, null=True)
    return_code = models.IntegerField(null=True)
    stdout = models.BinaryField(blank=True, null=True)
    stderr = models.BinaryField(blank=True, null=True)

    def __str__(self):
        return f"{str(self.id)}"

    class Meta:
        managed = False
        db_table = 'instance'
        unique_together = (('run', 'filename', 'boundary'),)


class Detection(models.Model):
    id = models.BigAutoField(primary_key=True)
    instance = models.ForeignKey(Instance, models.DO_NOTHING)
    run = models.ForeignKey(Run, models.DO_NOTHING)
    name = models.TextField(blank=True, null=True)
    access_url = models.TextField(blank=False, null=False)
    access_format = models.TextField(blank=False, null=False)
    x = PostgresDecimalField()
    y = PostgresDecimalField()
    z = PostgresDecimalField()
    x_min = models.IntegerField(blank=True, null=True)
    x_max = models.IntegerField(blank=True, null=True)
    y_min = models.IntegerField(blank=True, null=True)
    y_max = models.IntegerField(blank=True, null=True)
    z_min = models.IntegerField(blank=True, null=True)
    z_max = models.IntegerField(blank=True, null=True)
    n_pix = models.IntegerField(blank=True, null=True)
    f_min = PostgresDecimalField(blank=True, null=True)
    f_max = PostgresDecimalField(blank=True, null=True)
    f_sum = PostgresDecimalField(blank=True, null=True)
    rel = PostgresDecimalField(blank=True, null=True)
    rms = PostgresDecimalField(blank=True, null=True)
    w20 = PostgresDecimalField(blank=True, null=True)
    w50 = PostgresDecimalField(blank=True, null=True)
    ell_maj = PostgresDecimalField(blank=True, null=True)
    ell_min = PostgresDecimalField(blank=True, null=True)
    ell_pa = PostgresDecimalField(blank=True, null=True)
    ell3s_maj = PostgresDecimalField(blank=True, null=True)
    ell3s_min = PostgresDecimalField(blank=True, null=True)
    ell3s_pa = PostgresDecimalField(blank=True, null=True)
    kin_pa = PostgresDecimalField(blank=True, null=True)
    err_x = PostgresDecimalField(blank=True, null=True)
    err_y = PostgresDecimalField(blank=True, null=True)
    err_z = PostgresDecimalField(blank=True, null=True)
    err_f_sum = PostgresDecimalField(blank=True, null=True)
    ra = PostgresDecimalField(blank=True, null=True)
    dec = PostgresDecimalField(blank=True, null=True)
    freq = PostgresDecimalField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    l = PostgresDecimalField(blank=True, null=True)  # noqa
    b = PostgresDecimalField(blank=True, null=True)
    v_rad = PostgresDecimalField(blank=True, null=True)
    v_opt = PostgresDecimalField(blank=True, null=True)
    v_app = PostgresDecimalField(blank=True, null=True)
    unresolved = models.BooleanField()
    wm50 = PostgresDecimalField(null=True)
    x_peak = models.IntegerField(null=True)
    y_peak = models.IntegerField(null=True)
    z_peak = models.IntegerField(null=True)
    ra_peak = PostgresDecimalField(null=True)
    dec_peak = PostgresDecimalField(null=True)
    freq_peak = PostgresDecimalField(null=True)
    l_peak = PostgresDecimalField(null=True)
    b_peak = PostgresDecimalField(null=True)
    v_rad_peak = PostgresDecimalField(null=True)
    v_opt_peak = PostgresDecimalField(null=True)
    v_app_peak = PostgresDecimalField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'detection'
        ordering = ("x",)
        unique_together = (('ra', 'dec', 'freq', 'instance', 'run'),)


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    detection = models.ForeignKey(Detection, models.DO_NOTHING)
    cube = models.BinaryField(blank=True, null=True)
    mask = models.BinaryField(blank=True, null=True)
    mom0 = models.BinaryField(blank=True, null=True)
    mom1 = models.BinaryField(blank=True, null=True)
    mom2 = models.BinaryField(blank=True, null=True)
    chan = models.BinaryField(blank=True, null=True)
    snr = models.BinaryField(blank=True, null=True)
    spec = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
        unique_together = (('detection',),)


class Source(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'source'
        unique_together = (('name', ),)


class SourceDetection(models.Model):
    id = models.BigAutoField(primary_key=True)
    source = models.ForeignKey(Source, models.DO_NOTHING)
    detection = models.ForeignKey(Detection, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'source_detection'
        unique_together = (('detection', ),)


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField()
    author = models.CharField(max_length=128)
    detection = models.ForeignKey(Detection, models.DO_NOTHING)
    added_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True)

    class Meta:
        managed = False
        db_table = 'comment'


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(null=True)
    added_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tag'


class TagSourceDetection(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.ForeignKey(Tag, models.DO_NOTHING)
    source_detection = models.ForeignKey(SourceDetection, models.DO_NOTHING)
    author = models.TextField()
    added_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tag_source_detection'
