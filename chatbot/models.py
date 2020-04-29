from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords

class HistoricalQuestion(models.Model):
    class Meta:
        abstract = True 

    # Used for diffing in templates
    def previous_and_current_text(self):
        if self.prev_record:
            prev_text = self.prev_record.text 
        else:
            prev_text = '' 
        return prev_text, self.text

    def answers_for_version(self):
        if self.next_record:
            return self.history_object.answer_set.filter(create_date__range = [self.history_date, self.next_record.history_date])

        return self.history_object.answer_set.filter(create_date__gte = self.history_date)

class Question(models.Model):
    text = models.TextField()
    history = HistoricalRecords(bases=[HistoricalQuestion])

    def __str__(self):
        return self.text

class Answer(models.Model):
    text = models.CharField("your answer", max_length=128)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    def question_text(self):
        return self.question.history.as_of(self.create_date).text


