from django.db import models
# ORM stands for object relational mappings
# it is the implimentation which helps us map the operations in a database
# with constructs in python


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=256)
    roll_number = models.IntegerField(primary_key=True)
    date_of_birth = models.DateTimeField()
