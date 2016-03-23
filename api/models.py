from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)

class Student(Person):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(max_length=2,
                                      choices=YEAR_IN_SCHOOL_CHOICES,
                                      default=FRESHMAN)

    # Departmens of IUT
    CSE = 'CSE'
    ICE = 'ICE'
    DEPARTMENT_CHOICES = (
        (CSE, 'Computer Science and Engineering'),
        (ICE, 'Information and Communication Engineering')
    )
    student_department = models.CharField(max_length=10,
                                          choices=DEPARTMENT_CHOICES,
                                          default=CSE)

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)
    def __str__(self):
        return self.first_name +' '+ self.last_name

    class Meta:
        verbose_name = 'student'
