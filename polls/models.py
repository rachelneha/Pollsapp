import datetime
from django.utils import timezone
from django.db import models
from django.contrib import admin


# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date Published")

    def __str__(self):
        return self.question

    @admin.display(
        boolean = True,
        ordering="pub_date",
        description="Published Recently"
    )

    def wasPublishedRecently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    ques = models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice

class Difficulty(models.Model):
    DIFF_STATUS =[
        ("H","HARD"),
        ("M","MEDIUM"),
        ("S","SIMPLE"),
    ]
    quest=models.ForeignKey(Questions,on_delete=models.CASCADE)
    Difficulty_level=models.CharField(max_length=1,choices=DIFF_STATUS)

