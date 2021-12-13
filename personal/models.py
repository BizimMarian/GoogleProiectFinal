from django.db import models

# Create your models here.


class Filme(models.Model):
    Nume = models.CharField(max_length=20,blank=False)
    Filmul = models.CharField(max_length=100,blank=False)
    Nota = models.IntegerField()




    class Meta:
        abstract = True
    def __str__(self):
        return f'Filmul este {self.Filmul} are nota {self.Nota},scris de {self.Nume}'

class Horror(Filme):
    pass
class Comedie(Filme):
    pass
class Actiune(Filme):
    pass
class Drama(Filme):
    pass