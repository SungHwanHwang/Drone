from rest_framework import viewsets
from .serializers import FlySayingSerializer
from .models import FlySaying
import logging

logger = logging.getLogger(__name__)

class FlySayingView(viewsets.ModelViewSet) :
    queryset = FlySaying.objects.all()
    serializer_class = FlySayingSerializer