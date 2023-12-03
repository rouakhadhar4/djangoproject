from django.shortcuts import render, redirect
from .models import Etudiant
from .forms import EtudiantForm
from django.core.exceptions import MultipleObjectsReturned


def etudiant(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show_etudiant')
            except Exception as e:
                print(f"An error occurred: {e}")
                
        else:
            print(f"Form is not valid: {form.errors}")
    else:
        form = EtudiantForm()

    return render(request, 'etudiant.html', {'form': form})


def show_etudiant(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'show_etudiant.html', {'etudiants': etudiants})

def edit_etudiant(request, id):
    etudiant = Etudiant.objects.get(id=id)
    return render(request, 'edit_etudiant.html', {'etudiant': etudiant})

def update_etudiant(request, id):
    etudiant = Etudiant.objects.get(id=id)
    form = EtudiantForm(request.POST, instance=etudiant)
    if form.is_valid():
        form.save()
        return redirect("/show_etudiant")
    return render(request, 'edit_etudiant.html', {'etudiant': etudiant})

def delete_etudiant(request, id):
    etudiant = Etudiant.objects.get(id=id)
    etudiant.delete()
    return redirect("/show_etudiant")
 
def calculate_class_average():
    etudiants = Etudiant.objects.all()
    total_students = len(etudiants)
    
    if total_students > 0:
        total_average = sum(etudiant.moyenne for etudiant in etudiants) / total_students
        # Format the average to have three decimal places
        formatted_average = '{:.3f}'.format(total_average)
        return formatted_average
    else:
        return 0



def show_etudiant(request):
    etudiants = Etudiant.objects.all()

   
    admitted_count = len([etudiant for etudiant in etudiants if etudiant.moyenne > 10])
    rejected_count = len(etudiants) - admitted_count

  
    overall_average = calculate_class_average()

 
    return render(request, 'show_etudiant.html', {'etudiants': etudiants, 'admitted_count': admitted_count, 'rejected_count': rejected_count, 'overall_average': overall_average})


def search_etudiant(request):
    if request.method == "POST":
        cin = request.POST.get('cin', '')
        try:
            etudiant = Etudiant.objects.get(cin=cin)
            return render(request, 'show_etudiant.html', {'etudiants': [etudiant]})
        except Etudiant.DoesNotExist:
            message = "No Etudiant found with CIN: {}".format(cin)
            return render(request, 'show_etudiant.html', {'message': message})
        except MultipleObjectsReturned:
            etudiants = Etudiant.objects.filter(cin=cin)
            return render(request, 'show_etudiant.html', {'etudiants': etudiants})
    else:
        return redirect('show_etudiant')




       