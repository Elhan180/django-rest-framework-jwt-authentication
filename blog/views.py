from rest_framework import generics

from .models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
 



class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
    
        return Response({'message': 'You have access to this protected view!'})
