from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import *
from .models import *

class Authenticate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterAuthenticate
    permission_classes = [AllowAny]

class CreateNotes(generics.ListCreateAPIView):
    serializer_class = NotesDataSerailizer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user=self.request.user

        return NotesData.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class DeleteNotes(generics.DestroyAPIView):
    serializer_class = NotesDataSerailizer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return NotesData.objects.filter(author=user)

