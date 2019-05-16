import json
from django.db import models

class PlayerGroup(models.Model):
    player_group = models.IntegerField(primary_key=True, db_index=True)

    def __str__(self):
        return f'{self.player_group}'

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    player_group = models.ForeignKey(PlayerGroup, on_delete=models.CASCADE) # Each player is associated with a group
    score = models.IntegerField(default=0)
    lives = models.IntegerField(default=3)

    def __str__(self):
        return f'{self.username} from {self.player_group}'

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
    explanation = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.question

    # Create a json string to make an answer list
    def set_answer(self, answer_list):
        self.answer = json.dumps(answer_list)

    # Use json to transform the list in string form to a usable list
    def get_answer(self):
        return json.loads(self.answer)

    # Check if the given answer is part of the answer list
    def verify_answer(self, given_answer):
        correct_answer = self.get_answer()
        return given_answer in correct_answer
