from django import forms
from etudiant.models import Etudiant  # Replace 'etudiant' with the actual name of your Django app

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = "__all__"
