from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import PlayerGroup, Player, Question
from django.urls import path
from django.shortcuts import render, redirect
from django import forms
import csv
import io

# Register custom models
admin.site.register(PlayerGroup)
admin.site.register(Player)

# Unregister the default models so they don't show up in the admin page
admin.site.unregister(User)
admin.site.unregister(Group)

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

# Class view to customize the Question section to allow admins to upload csv to populate question table
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
            next(io_string)
            for col in csv.reader(io_string):
                _, created = Question.objects.update_or_create(
                    question = col[0],
                    choice_1 = col[1],
                    choice_2 = col[2],
                    choice_3 = col[3],
                    choice_4 = col[4]
                )
                new_question = Question.objects.filter(question=col[0]).first()
                new_question.set_answer(col[5])
                new_question.save()
            self.message_user(request, 'Le fichier a été ajouté')
            return redirect('/admin')
        form = CsvImportForm()
        context = {'form': form}
        return render(request, 'quiz/csv_form.html', context)
