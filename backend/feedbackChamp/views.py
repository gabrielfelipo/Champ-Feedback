from .models import champs
from rest_framework.viewsets import ModelViewSet
from .serializers import champsSerializer

# Create your views here.
class champsViewSet(ModelViewSet):
    queryset = champs.objects.all()
    serializer_class = champsSerializer