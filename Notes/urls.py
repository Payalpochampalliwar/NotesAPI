from .views import *
from django.urls import path

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name= 'note-detail'),
    path('delete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
            
]