from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno
# Create your views here.


def criar_aluno(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        
        return render(request, 'criar_aluno.html',{'status':status})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')

        if len(nome.strip()) == 0 or int(idade)<= 0:
            return redirect('/alunos/criar_aluno/?status=1') #status = 1 na URL



        aluno = Aluno(nome=nome, idade=idade, email=email)
        aluno.save()
        return redirect('/alunos/criar_aluno/?status=0')


def listar(request):
    return HttpResponse("Listei")
