from django.db import models

"""
usuario: fabricio
email:fabricio@gmail.com
senha: 12345678
usuario: Ricardo
email:ricardo@gmail.com
senha: 12345678
"""

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
