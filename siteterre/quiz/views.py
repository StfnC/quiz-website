from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import PlayerGroup, Player, Question
from .forms import PlayerForm
from random import shuffle

def home(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            player_group = form.cleaned_data['player_group']
            new_player = Player(username=username, player_group=player_group)
            new_player.save()
            request.session['player_id'] = new_player.id
        return redirect(reverse('quiz:question', args=[Question.objects.order_by('id').first().id]))
    form = PlayerForm()
    context = {'form': form}
    return render(request, 'quiz/home.html', context)

def question(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = [
                question.choice_1,
                question.choice_2,
                question.choice_3,
                question.choice_4
                ]
    shuffle(choices)
    question_answer = question.get_answer()
    player = Player.objects.get(id=request.session['player_id'])
    if request.method == 'POST':
        pass
    context = {
                'question': Question.objects.get(id=question_id),
                'question_choices': choices,
                'score': player.score,
                'lives': player.lives
                }
    return render(request, 'quiz/question.html', context)
