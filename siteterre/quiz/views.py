from django.shortcuts import render, redirect, reverse
from django.contrib import messages
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
    context = {
                'title': 'Accueil',
                'form': form
                }
    return render(request, 'quiz/home.html', context)

def question(request, question_id):
    last_question_id = Question.objects.order_by('id').reverse()[0].id
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
        given_answer = request.POST.get('choice')
        print(given_answer)
        print(question_answer)
        if given_answer in question_answer:
            player.increase_score(4)
        else:
            player.decrease_lives(1)
        player.save()
        messages.info(request, f'{question.explanation}')
        if question_id == last_question_id or player.lives == 0:
            return redirect(reverse('quiz:leaderboard', args=[player.player_group]))
        else:
            return redirect(reverse('quiz:question', args=[question_id + 1]))
    context = {
                'title': 'Question',
                'question': Question.objects.get(id=question_id),
                'question_choices': choices,
                'score': player.score,
                'lives': player.lives
                }
    return render(request, 'quiz/question.html', context)

def leaderboard(request, player_group):
    player_group = PlayerGroup.objects.get(player_group=player_group)
    players_in_group = player_group.player_set.order_by('score').reverse().all()
    context = {
                'title': f'Classement du groupe {player_group}',
                'player_group': player_group,
                'players_in_group': players_in_group
                }
    return render(request, 'quiz/leaderboard.html', context)
