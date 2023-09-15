from django import forms


class TaskCreationForm(forms.Form):
    title = forms.CharField(label='Titulo', max_length=255)
    content = forms.CharField(label='Detalle', widget=forms.Textarea())
