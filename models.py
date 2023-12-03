

from django.db import models

class Etudiant(models.Model):
    cin = models.CharField(max_length=20) 
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    moyenne = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
   

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        db_table = "etudiant"

