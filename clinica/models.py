from django.db import models


class Ocupacion(models.Model):
    codOcupacion = models.CharField(max_length=4, primary_key=True)
    desOcupacion = models.CharField(max_length=200)
    padre = models.IntegerField()

    class Meta:
        db_table = 'ocupacion'

    def __str__(self):
        return f"{self.codOcupacion}, {self.desOcupacion}"

class PrestadoresSalud(models.Model):
    codPrestadorSalud = models.CharField(max_length=12, primary_key=True)
    prestadoresSalud = models.CharField(max_length=12)

    class Meta:
        db_table = 'prestadoresSalud'

    def __str__(self):
        return f"{self.codPrestadores}, {self.prestadoresSalud}"



class VoluntaAnticipada(models.Model):
    VOLUNTAD = [
        ('01', 'Si'),
        ('02', 'No')
    ]
    idVoluntad = models.CharField(max_length=2, primary_key=True)
    docVoluntad = models.CharField(max_length=200, choices=VOLUNTAD)
    fecha = models.DateField(max_length=10)
    codPrestadorSalud =models.ForeignKey(PrestadoresSalud,max_length=12, on_delete=models.CASCADE)

    class Meta:
        db_table = 'voluntaAnticipada'

    def __str__(self):
        return f"{self.idVoluntad}, {self.docVoluntad} {self.fecha} {self.codPrestadorSalud}"

class Triage(models.Model):
    TRIAGE = [
        ('01', 'TRIAGE I'),
        ('02', 'TRIAGE II'),
        ('03', 'TRIAGE III'),
        ('04', 'TRIAGE IV'),
        ('05', 'TRIAGE V'),
    ]
    idTriage = models.AutoField(primary_key=True)
    fechaTriage = models.DateField()
    horaTriage = models.TimeField()
    ClasificacionTriage = models.CharField('Clasificacion de triage',max_length=2, choices= TRIAGE )

    class Meta:
        db_table = 'triage'

    def __str__(self):
        return f"{self.idTriage}, {self.horaTriage}, {self.ClasificacionTriage}"

class ModalidadServicios(models.Model):
    codModalidadServicios = models.CharField(max_length=2, primary_key=True)
    ModalidadServicios = models.CharField(max_length=100,unique=True,null=True,blank=True)

    class Meta:
        db_table = 'modalidadServicios'

    def __str__(self):
        return f"{self.codModalidadServicios}, {self.ModalidadServicios}"

