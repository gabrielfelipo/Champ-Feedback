from rest_framework.serializers import ModelSerializer
from .models import champs

class champsSerializer(ModelSerializer):
    class Meta:
        model= champs
        fields = ['id', 'name', 'rating', 'comment']