from django.db import models

class Diagnostico(models.Model):
    codDiagnostico = models.CharField(primary_key=True, max_length=4),
    diagnostico = models.CharField(max_length=200),
    padre = models.IntegerField(max_length=5)

    class Meta:
        db_table = 'diagnostico'