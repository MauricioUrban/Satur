from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):

    EMPRESAS = [
        ('Don Satur', 'Empresa 1'),
        ('Mani King', 'Empresa 2'),
        ('Leiva', 'Empresa 3'),
        ('Hojalmar', 'Empresa 4'),
        ('Mafalda', 'Empresa '),
    ]

    empresa = forms.ChoiceField(choices=EMPRESAS, widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    class Meta:
        model = Pedido
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'empresa': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
