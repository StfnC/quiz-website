from django.forms import ModelForm
from quiz.models import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['username', 'player_group']
