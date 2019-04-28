from django.shortcuts import render, redirect
from .models import Player
from .forms import PlayerForm

def home(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            player_group = form.cleaned_data['player_group']
            new_player = Player(username=username, player_group=player_group)
            new_player.save()
            request.session['player_id'] = new_player.id
        return redirect('/home')
    form = PlayerForm()
    context = {'form': form}
    return render(request, 'quiz/home.html', context)
