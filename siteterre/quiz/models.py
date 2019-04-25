import json
from django.db import models

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    group = models.IntegerField(db_index=True)
    score = models.IntegerField(default=0)
    lives = models.IntegerField(default=3)

    def __str__(self):
        return f'{self.username} from {self.group}'

    def increase_score(self, increment):
        self.score += increment

    def decrease_lives(self, decrement):
        self.lives -= decrement

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=300)
    choice_1 = models.CharField(max_length=300)
    choice_2 = models.CharField(max_length=300)
    choice_3 = models.CharField(max_length=300)
    choice_4 = models.CharField(max_length=300)
    answer = models.CharField(max_length=500, default='[]')

    def __str__(self):
        return self.question

    def set_answer(self, answer_list):
        self.answer = json.dumps(answer_list)

    def get_answer(self):
        return json.loads(self.answer)
