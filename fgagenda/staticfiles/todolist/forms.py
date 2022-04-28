#from msilib.schema import Class
#from tkinter import Widget
from django import forms
from .models import ToDoList
from django.core.exceptions import ValidationError
from meta.models import Meta


class ToDoForms(forms.ModelForm):
    
#    def min_validation(value):
#        if len(value) < 1:
#            raise ValidationError("{} não é valido, o campo não deve ser vazio.". format(value))
    
#    def __init__(self, *args, **kwargs):
#        super(ToDoList, self).__init__(*args, **kwargs)
#        self.fields["tarefa"].validators.append(min_validation)    
 
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
        super(ToDoForms, self).__init__(*args, **kwargs)
        self.fields['meta'] = forms.ChoiceField(
            required=True, label="Meta", 
            choices=self.get_meta_names
        )

    def get_meta_names(self):
        names = []
        for meta in Meta.objects.all():
            names.append((meta.id, meta.nome))
        
        return names

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