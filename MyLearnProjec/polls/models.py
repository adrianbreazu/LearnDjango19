import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    # restrict the field lenght to 200 characters
    question_text = models.CharField(max_length=200)
    # get the human-readable name date published
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()


class Choice(models.Model):
    # note a relation as foreign key to class/table Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # restrict the field lenght to 200
    choice_text = models.CharField(max_length=200)
    # set the default value to 0
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
