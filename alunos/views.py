from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def criar_aluno(request):
    print(request.method)
    return render(request,'criar_aluno.html')

def listar(request):
    return HttpResponse("Listei")