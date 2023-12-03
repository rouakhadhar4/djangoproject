from django.urls import path
from . import views

urlpatterns = [
    path('etudiant/', views.etudiant, name='etudiant'),
    path('show_etudiant/', views.show_etudiant, name='show_etudiant'),
    path('edit_etudiant/<int:id>', views.edit_etudiant),
    path('update_etudiant/<int:id>', views.update_etudiant),
    path('delete_etudiant/<int:id>', views.delete_etudiant),
    path('search_etudiant/', views.search_etudiant, name='search_etudiant'),
]
