from django.db import models
import random

# Create your models here.
class Quizes (models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text='Quiz Duration')
    requiered_score_to_pass = models.IntegerField(help_text='Pass %')

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        return questions[:self.number_of_questions]
    class Meta:
        verbose_name_plural = 'Quizes'