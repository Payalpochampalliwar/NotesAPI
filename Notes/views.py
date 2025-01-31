from django.shortcuts import render
from .models import *
from .serializers import NoteSerializer
from rest_framework import generics, permissions

# Create your views here.
class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = NoteSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    
class NoteDeleteView(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
