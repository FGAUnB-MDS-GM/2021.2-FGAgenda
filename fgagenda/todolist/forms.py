#from msilib.schema import Class
#from tkinter import Widget
from django import forms
from .models import ToDoList
from django.core.exceptions import ValidationError
from meta.models import Meta


class ToDoForms(forms.ModelForm):
    
    class Meta:
        model = ToDoList
        fields = [
            "meta",
            "tarefa"
        ]
        widgets = {
            "meta": forms.Select(attrs={
                'class': "cria-meta-input",
                'placeholder': 'Meta',
                'width': '80%',
            }),
            "tarefa": forms.TextInput(attrs={
                'class': "cria-meta-input",
                'placeholder': 'Tarefa'
            })
        }

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        super().__init__(*args, **kwargs)
        self.fields['meta'] = forms.ChoiceField(
            required=True, label="Meta",
            choices=self.get_meta_names
        )
        

    def get_meta_names(self):
        nomes = []
        
        for meta in Meta.objects.filter(pk=self.pk):
            nomes.append((meta.id, meta.nome))
        
        return nomes

    def clean_meta(self):
        data = self.cleaned_data['meta']

        if not Meta.objects.filter(pk=data).exists():
            raise ValidationError("A meta não existe!")
        else:
            data = Meta.objects.get(pk=data)

        return data
    
    def clean(self):
        cleaned_data = super(ToDoForms, self).clean()

        meta = cleaned_data.get('meta')
        tarefa = cleaned_data.get('tarefa')

        if ToDoList.objects.filter(
            meta=meta,
            tarefa=tarefa
        ).exists():
            raise ValidationError("A tarefa já existe!")

        return cleaned_data

class EditaToDoList(forms.ModelForm):
    
    class Meta:
        model = ToDoList
        fields = [
            "tarefa"
        ]
        widgets = {
            "tarefa": forms.TextInput(attrs={
                'class': "cria-meta-input",
                'placeholder': 'Tarefa'
            })
        }

    def __init__(self, *args, **kwargs):
        self.meta_pk = kwargs.pop('meta_pk', None)
        request = kwargs.pop('request', None)
        self.conteudo_nova_tarefa = request.POST['conteudo']
        #self.request.POST['conteudo']
        super().__init__(*args, **kwargs)

    def clean_tarefa(self):
        data = self.cleaned_data['tarefa']

        if not ToDoList.objects.filter(pk=data).exists():
            raise ValidationError("A tarefa não existe!")
        else:
            data = ToDoList.objects.get(pk=data)

        return data
    
    def clean(self):
        cleaned_data = super(EditaToDoList, self).clean()

        meta = Meta.objects.get(pk=self.meta_pk)
        tarefa = cleaned_data.get('tarefa')

        if ToDoList.objects.filter(meta=meta,tarefa=tarefa).exists():
            raise ValidationError("A tarefa já existe!")
        else:
            ToDoList.objects.filter(tarefa=tarefa).update(tarefa=self.conteudo_nova_tarefa)

        return cleaned_data