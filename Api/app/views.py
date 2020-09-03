from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job, Applicant, Skill
from .serializer import JobSerializer, ApplicantSerializer, SkillSerializer

# Create your views here.


class Jobs(APIView):

    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response([{"id": _.id, "name": _.name} for _ in Job.objects.all()])


class Applicants(APIView):

    def post(self, request):
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response([{"id": _.id, "name": _.name, "email": _.email, "website":_.website, "cover_letter":_.cover_letter, "job_id":_.job_id.id} for _ in Applicant.objects.all()])


class Skills(APIView):

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response([{"id": _.id, "name": _.name, "applicant_id": _.applicant_id.id} for _ in Skill.objects.all()])


