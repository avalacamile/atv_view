from django.shortcuts import render
from .models import *

# Create your views here.
def Index (request):
    alunos = Aluno.objects.all()
    contexto = {
        'aluno': alunos,
    }
    return render(request, 'pessoa/index.html',contexto)
