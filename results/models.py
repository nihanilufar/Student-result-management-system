from django.db import models

class student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=15,unique=True)
    batch = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=15,unique=True)
    max_marks = models.Integration(default=100)

    def __str__(self):
        return self.name

class Result(models.Model):
    student = models.Foreignkey(student,on_delete=models.CASCADE,related_name='results')
    subject = models.Foreignkey(Subject,on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    exam_date = models.DateField(auto_now_add=True)

    class meta:
        unique_together = ('student','subjects')


    def __str__(self):
        return f"{self.student} : {self.subject}"



                     

