from django import forms
from .models import Aula, Evento as EventoModel
from django.utils.timezone import datetime, timedelta
from django.core.exceptions import ValidationError

DIAS_SEMANA = (
    ("2", "Segunda"),
    ("3", "Terça"),
    ("4", "Quarta"),
    ("5", "Quinta"),
    ("6", "Sexta"),
    ("7", "Sabado"),
    ("8", "Domingo"),
)

class CriaEventoForm(forms.ModelForm):
    
    class Meta:
        dia_seguinte = datetime.today() + timedelta(days=1)
        dia_seguinte = dia_seguinte.replace(hour=0, minute=0, second=0)
        dia_maximo = datetime.today() + timedelta(days=7)
        model = EventoModel
        fields = [
            'nome',
            'descricao',
            'dia',
            'frequencia',
            'horaInicio',
            'horaFim'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': "criar-evento-input",
                'placeholder': 'Nome do Evento'
            }),
            'descricao': forms.Textarea(attrs={
                'class': "criar-evento-input",
                'placeholder': 'Descrição'
            }),
            'dia': forms.DateInput(attrs={
                'type': "date",          
                'class': "criar-evento-input",
                'min': dia_seguinte.strftime("%Y-%m-%d"),
                'max': dia_maximo.strftime("%Y-%m-%d")
            }),
            'horaInicio': forms.TimeInput(attrs={
                'type': "time",          
                'class': "criar-evento-input"
            }),
            'horaFim': forms.TimeInput(attrs={
                'type': "time",          
                'class': "criar-evento-input",
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CriaEventoForm, self).__init__(*args, **kwargs)
        self.fields['frequencia'] = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=DIAS_SEMANA,
    ) 

    def clean(self):
        cleaned_data = super(CriaEventoForm, self).clean()
        hora_inicio = cleaned_data.get('horaInicio')
        hora_fim = cleaned_data.get('horaFim')
        
        if hora_inicio > hora_fim:
            raise ValidationError({'horaInicio': ["Hora Inicio não pode ser depois da Hora Fim!"]})

        return cleaned_data

class EditaEventoForm(forms.ModelForm):

    class Meta:
        dia_seguinte = datetime.today() + timedelta(days=1)
        dia_seguinte = dia_seguinte.replace(hour=0, minute=0, second=0)
        dia_maximo = datetime.today() + timedelta(days=7)
        model = EventoModel
        fields = [
            'nome',
            'descricao',
            'dia',
            'frequencia',
            'horaInicio',
            'horaFim'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': "criar-evento-input",
                'placeholder': 'Nome do Evento'
            }),
            'descricao': forms.Textarea(attrs={
                'class': "criar-evento-input",
                'placeholder': 'Descrição'
            }),
            'dia': forms.DateInput(attrs={
                'type': "date",          
                'class': "criar-evento-input",
                'min': dia_seguinte.strftime("%Y-%m-%d"),
                'max': dia_maximo.strftime("%Y-%m-%d")
            }),
            'horaInicio': forms.TimeInput(attrs={
                'type': "time",          
                'class': "criar-evento-input"
            }),
            'horaFim': forms.TimeInput(attrs={
                'type': "time",          
                'class': "criar-evento-input"
            }),
        }

    def __init__(self, *args, **kwargs):
        super(EditaEventoForm, self).__init__(*args, **kwargs)
        self.fields['frequencia'] = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=DIAS_SEMANA,
    ) 

    def clean(self):
        cleaned_data = super(EditaEventoForm, self).clean()
        hora_inicio = cleaned_data.get('horaInicio')
        hora_fim = cleaned_data.get('horaFim')
        
        if hora_inicio > hora_fim:
            raise ValidationError({'horaInicio': ["Hora Inicio não pode ser depois da Hora Fim!"]})

        return cleaned_data

class CriaAulaForm(forms.ModelForm):
    
    class Meta:
        model = Aula
        fields = [
            'nome',
            'descricao',
            'horarioAula'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': "criar-aula-input",
                'placeholder': 'Nome da Aula'
            }),
            'descricao': forms.Textarea(attrs={
                'class': "criar-aula-input",
                'placeholder': 'Descrição'
            }),
            'horarioAula': forms.TextInput(attrs={          
                'class': "criar-aula-input",
                'placeholder': '35T12'
            })
        }

    """ def __init__(self, *args, **kwargs):
        super(CriaAulaForm, self).__init__(*args, **kwargs)
        self.fields['frequencia'] = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=DIAS_SEMANA,
    )  """

    """ def clean_horarioAula(self):
        data = self.cleaned_data['horarioAula']
        turnos_unb = ['M', 'T', 'N']
        contador_turno_m = 0
        contador_turno_t = 0
        contador_turno_n = 0
        turno = ""

        print(type(data))

        if len(data) < 4:
            self.add_error('horarioAula', "O mínimo de caracteres são 4!")
            #raise ValidationError({'horarioAula': ["O mínimo de caracteres são 4!"]})

        #Verifica se existe um turno M, T ou N no horário
        if turnos_unb[0] in data:
            for letra in data:
                if letra == turnos_unb[0]:
                    contador_turno_m += 1
            if contador_turno_m > 1:
                self.add_error('horarioAula', "O horário da Aula não está na fomatação correta!")
                #raise ValidationError({'horarioAula': ["O horário da Aula não está na fomatação correta!"]})
            turno += turnos_unb[0]
        elif turnos_unb[1] in data:
            for letra in data:
                if letra == turnos_unb[1]:
                    contador_turno_m += 1
            if contador_turno_m > 1:
                self.add_error('horarioAula', "O horário da Aula não está na fomatação correta!")
                #raise ValidationError({'horarioAula': ["O horário da Aula não está na fomatação correta!"]})
            turno += turnos_unb[1]
        elif turnos_unb[2] in data:
            for letra in data:
                if letra == turnos_unb[2]:
                    contador_turno_m += 1
            if contador_turno_m > 1:
                self.add_error('horarioAula', "O horário da Aula não está na fomatação correta!")
                #raise ValidationError({'horarioAula': ["O horário da Aula não está na fomatação correta!"]})
            turno += turnos_unb[2]
        else:
            self.add_error('horarioAula', "O turno da Aula não foi especificado!")
            #raise ValidationError({'horarioAula': ["O turno da Aula não foi especificado!"]})

        #dias_semana, horarios_dia = data.split(turno)[0], data.split(turno)[1]

        return data """

    """ def clean(self):
        cleaned_data = super(CriaAulaForm, self).clean()
        hora_inicio = cleaned_data.get('horaInicio')
        hora_fim = cleaned_data.get('horaFim')
        
        if hora_inicio > hora_fim:
            raise ValidationError({'horaInicio': ["Hora Inicio não pode ser depois da Hora Fim!"]})

        return cleaned_data """

class EditaAulaForm(forms.ModelForm):
    
    class Meta:
        model = Aula
        fields = [
            'nome',
            'descricao',
            'horarioAula'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': "criar-aula-input",
                'placeholder': 'Nome da Aula'
            }),
            'descricao': forms.Textarea(attrs={
                'class': "criar-aula-input",
                'placeholder': 'Descrição'
            }),
            'horarioAula': forms.TextInput(attrs={          
                'class': "criar-aula-input",
                'placeholder': '35T12'
            })
        }