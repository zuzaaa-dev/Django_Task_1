from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'text', 'end_date', 'priority']
        labels = {
            'title': 'Заголовок',
            'text': 'Описание',
            'end_date': 'Дата окончания',
            'priority': 'Приоритет',
        }
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
        self.fields['priority'].widget.attrs.update({'class': 'form-control'})
