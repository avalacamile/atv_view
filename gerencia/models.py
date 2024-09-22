from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    email = models.EmailField()
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)

    def __str__(self):
        return self.nome