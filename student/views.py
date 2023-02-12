from django.shortcuts import render
from rest_framework.views import APIView
from student.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from student.models import Student

# Create your views here.


class StudentAPIView(APIView):

    def get(self, request, pk=None):
        print(pk)
        if not pk:
            student = Student.objects.all()
            serializer = StudentSerializer(instance=student, many=True)
        else:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(instance=student)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(
            instance=student, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
