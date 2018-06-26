from django.db import models

class TemporalModel(models.Model):
    vf = models.DateTimeField(db_column='VF') 
    vt = models.DateTimeField(db_column='VT') 
    vflag = models.IntegerField(db_column='VFlag')
    vu = models.CharField(db_column='VU', max_length=10, blank=True, null=True)
    djangoid = models.AutoField(db_column='djangoID', primary_key=True)

    class Meta:
        abstract = True

class TemporalModelManualDjangoID(models.Model):
    vf = models.DateTimeField(db_column='VF') 
    vt = models.DateTimeField(db_column='VT') 
    vflag = models.IntegerField(db_column='VFlag')
    vu = models.CharField(db_column='VU', max_length=10, blank=True, null=True)

    class Meta:
        abstract = True