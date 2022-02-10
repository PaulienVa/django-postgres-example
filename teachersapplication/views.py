from django.shortcuts import render

from teachersapplication.models import Teacher
from rest_framework import viewsets

from teachersapplication.serializer import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
