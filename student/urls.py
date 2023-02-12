from django.urls import path
from student.views import StudentAPIView


urlpatterns = [
    path('student/', StudentAPIView.as_view(), name='create-student'),
    path('student/<int:pk>/', StudentAPIView.as_view(), name='retrieve-student')
]
