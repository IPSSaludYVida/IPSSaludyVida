from django.db import models

class OpocisionDonacion(models.Model):
    idDonacion = models.IntegerField(primary_key=True)
    manifestacionOpo = models.CharField(max_length=2)
    fechaDonacion = models.DateField()

    class Meta:
        db_table = 'opocisionDonacion'


class Etnia(models.Model):
    codEtnia = models.IntegerField(primary_key=True)
    etnia = models.CharField(max_length=50)

    class Meta:
        db_table = 'etnia'

class ComunidadEtnia(models.Model):
    codComunidadEtnia = models.IntegerField(primary_key=True)
    desComunidad = models.CharField(max_length=50)
    codEtnia =models.ForeignKey(Etnia, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'comunidadEtnia'

class Pais(models.Model):
    idPais = models.IntegerField(primary_key=True)
    nomPais = models.CharField(max_length=200)

    class Meta:
        db_table = 'pais'

class Discapacidades (models.Model):
    codDiscapacidad =models.IntegerField(primary_key=True)
    calDiscapacidad = models.CharField(max_length=50)

    class Meta:
        db_table = 'discapacidades'

class EntidadSalud(models.Model):
    codEntidad =models.IntegerField(primary_key=True)
    nomEntidad =models.CharField(max_length=200)

    class Meta:
        db_table = 'entidadSalud'

