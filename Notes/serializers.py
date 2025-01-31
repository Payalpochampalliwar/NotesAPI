from rest_framework import serializers
from .models import *

class NoteSerializer(serializers.ModelSerializer):
    class meta:
        model = Note
        fields = '__all__'