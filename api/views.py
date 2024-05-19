from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,CreateAPIView,ListCreateAPIView
from .serializers import *
from .models import *
import json

@api_view(["GET","POST"])
def home(req,*args,**kwargs):
    serializer=ProductSerializer(data=req.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    return Response({"message":"invalide data"})
class Createapi(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        print(serializer.validated_data.get('content'))
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=serializer.validated_data.get('title')
        serializer.save(content=content)
class ProductDetailsAPI(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListClass(ListCreateAPIView):
    queryset =Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=serializer.validate_data.get('title')
            serializer.save(content=content)

