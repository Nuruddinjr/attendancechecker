from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Student
            fields = ('pk', 'last_name', 'first_name', 'year_in_school', 'student_department')
