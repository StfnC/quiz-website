from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import PlayerGroup, Player, Question
from django.urls import path
from django.shortcuts import render, redirect
from django import forms
from random import randrange
import csv
import io

admin.site.site_header = 'Quiz Admin'
admin.site.site_title = 'Quiz Admin'
admin.site.index_title = 'Quiz Admin'

# Register custom models
admin.site.register(Player)

# Unregister the default models so they don't show up in the admin page
admin.site.unregister(User)
admin.site.unregister(Group)

class NewGroupForm(forms.Form):
    group_num = forms.IntegerField(label='Numéro du groupe')

# Classe to customize the PlayerGroup section to add 'Create New Group' button
@admin.register(PlayerGroup)
class PlayerGroupAdmin(admin.ModelAdmin):
    change_list_template = 'quiz/group_change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('create_new_group/', self.create_new_group)
        ]
        return my_urls + urls

    def create_new_group(self, request):
        if request.method == 'POST':
            form = NewGroupForm(request.POST)
            if form.is_valid():
                group_num = form.cleaned_data['group_num']
                random_tail = randrange(100, 1000) # Generate a random number between 100 and 999
                group = group_num * 1000 + random_tail # Concatenate the random number to the group number chosen by the admin
                new_player_group = PlayerGroup(player_group=group)
                new_player_group.save()
                self.message_user(request, f'Le groupe {group} a été créé', extra_tags='safe')
            return redirect('/admin')
        form = NewGroupForm()
        context = {'form': form}
        return render(request, 'quiz/new_group_form.html', context)

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

# Class to customize the Question section to allow admins to upload csv to populate question table
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    change_list_template = 'quiz/question_change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import_csv/', self.import_csv)
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == 'POST':
            csv_file = request.FILES['csv_file']
            data_set = csv_file.read().decode('utf-8')
            io_string = io.StringIO(data_set)
            next(io_string) # Skip the first line of the csv as it only contains the name of each col
            for row in csv.reader(io_string):
                _, created = Question.objects.update_or_create(
                    question = row[0],
                    choice_1 = row[1],
                    choice_2 = row[2],
                    choice_3 = row[3],
                    choice_4 = row[4],
                    explanation = row[6]
                )
                new_question = Question.objects.get(question=row[0])
                new_question.set_answer(row[5])
                new_question.save()
            self.message_user(request, 'Le fichier a été ajouté')
            return redirect('/admin')
        form = CsvImportForm()
        context = {
                    'form': form
                    }
        return render(request, 'quiz/csv_form.html', context)
