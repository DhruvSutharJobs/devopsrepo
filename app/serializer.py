from rest_framework import serializers
from app.models import Todos

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Todos
        fields='__all__'