from django.shortcuts import render


def login_user(request):
    if request.method == 'GET':
        template = 'login.html'
        context = {}

        return render(request, template, context)