from django.db import models
from django.contrib.auth.models import User

class EvolutionLine(models.Model):
    
    #Relacionamento com a entidade User
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    
    #Fases evolutivas dos digimons representadas em colunas da tabela
    baby_i_id = models.PositiveIntegerField(null=True, blank=True)
    baby_ii_id = models.PositiveIntegerField(null=True, blank=True)
    child_id = models.PositiveIntegerField(null=True, blank=True)
    adult_id = models.PositiveIntegerField(null=True, blank=True)
    perfect_id = models.PositiveIntegerField(null=True, blank=True)
    ultimate_id = models.PositiveIntegerField(null=True, blank=True)
    super_ultimate_id = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return EvolutionLine.name