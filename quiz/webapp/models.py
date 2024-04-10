from django.db import models
from .models import *

auth_list = (
    ('allow' , "allow"),
    ('block' , "block"),
    
)

college_list = (
    ('SRIKALIKI' , "SREENIVASA DEGREE COLLLEGE ,KALIKIRI"),
    ('SGPLR' , "S.G.DEGREE COLLEGE , PILEAR"),

)

class Student(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    test_no = models.IntegerField()
    test_avg = models.IntegerField()
    total = models.IntegerField()
    auth =  models.CharField(choices = auth_list , max_length = 20)
    college = models.CharField(choices = college_list , max_length = 20)
    studentId = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Test_questions(models.Model):
    question = models.CharField(max_length=500)
    a = models.CharField(max_length=500)
    b = models.CharField(max_length=500)
    c = models.CharField(max_length=500)
    d = models.CharField(max_length=500)
    ans =models.CharField(max_length=1)
    def __str__(self):
        return self.question
    
class Test(models.Model):
    user_id = models.CharField(max_length=12)
    name = models.CharField(max_length=50)
    marks  = models.CharField(max_length=2)
    test_no = models.CharField(max_length=2)
    def __str__(self):
        return self.name