from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #ForeignKey : connect another model
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField()



