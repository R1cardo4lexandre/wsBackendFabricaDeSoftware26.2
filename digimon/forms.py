from django import forms
from .models import EvolutionLine

class EvolutionLineForm(forms.ModelForm):
    class Meta:
        
        model = EvolutionLine
        fields = [
            'name',
            'baby_i_id',
            'baby_ii_id',
            'child_id',
            'adult_id',
            'perfect_id',
            'ultimate_id',
            'super_ultimate_id',
        ]
        
        labels = {
            'name': 'Nome da linha evolutiva',
            'baby_i_id': 'Nível Baby I',
            'baby_ii_id': 'Nível Baby II',
            'child_id': 'Nível Child',
            'adult_id': 'Nível Adulto',
            'perfect_id': 'Nível Perfeito',
            'ultimate_id': 'Nível Ultimate',
            'super_ultimate_id': 'Nível Super Ultimate',
        }