from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return f'Question: {self.question}'


class Choice(models.Model):
    choice_text = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'Awnser: {self.choice_text}'



