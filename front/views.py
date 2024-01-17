import datetime
from django.shortcuts import render


def index(request):
    posts = [
        {
            'author': '<Вася Васечкин>',
            'title': 'Пост 1',
            'date': datetime.date(2020, 3, 12),
            'text': 'Случайный текст случайный текст '
                    'Случайный текст случайный текст '
                    'Случайный текст случайный текст '
        },
        {
            'author': '<Петя Петичкин>',
            'title': 'Пост 2',
            'date': datetime.date(2022, 6, 1),
            'text': 'Случайный текст2 случайный текст2 '
                    'Случайный текст2 случайный текст2 '
                    'Случайный текст2 случайный текст2 '
        }
    ]
    return render(request,
                  'index1.html',
                  {'title': 'Главная',
                   'posts': posts})
