from django.shortcuts import render


def home(request):
    speakers = [
        {'name': 'Grace Hopper', 'photo': 'https://encurtador.com.br/hwzDG'},
        {'name': 'Alan Turing', 'photo': 'https://encurtador.com.br/nDFI7'}
    ]
    return render(request, 'index.html', {'speakers': speakers})