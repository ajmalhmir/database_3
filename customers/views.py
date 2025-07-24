from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing customer instances.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
