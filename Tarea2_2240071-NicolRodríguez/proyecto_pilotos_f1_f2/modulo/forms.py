from django import forms

from .models import Piloto


class PilotoForm(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = [
            'nombre',
            'categoria',
            'escuderia',
            'edad',
            'anio_debut',
            'nacionalidad',
            'descripcion',
            'imagen',
        ]
        widgets = {
            'nombre': forms.TextInput(
                attrs={'placeholder': 'Ej. Lando Norris'}
            ),
            'escuderia': forms.TextInput(
                attrs={'placeholder': 'Ej. McLaren'}
            ),
            'edad': forms.NumberInput(attrs={'min': 16, 'max': 70}),
            'anio_debut': forms.NumberInput(
                attrs={'min': 1950, 'max': 2100}
            ),
            'nacionalidad': forms.TextInput(
                attrs={'placeholder': 'Ej. Británica'}
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Breve descripción del piloto...',
                }
            ),
            'imagen': forms.TextInput(
                attrs={'placeholder': 'max-verstappen-2026.png'}
            ),
        }
