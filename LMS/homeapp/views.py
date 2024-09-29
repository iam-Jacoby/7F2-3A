from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def home(request):
    return HttpResponse("Hello world!")