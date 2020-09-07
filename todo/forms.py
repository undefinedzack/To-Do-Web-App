from django import forms

class new_task_form(forms.Form):
    text = forms.CharField(max_length=500,
                           widget = forms.TextInput(
                               attrs={ 'class' : 'form-control',
                                       'aria-label' : 'To Do',
                                       'aria-describedby' : 'inputGroup-sizing-default',
                                       'placeholder' : 'task?'}
                           ) )

    description = forms.CharField(max_length=2000,
                                  widget = forms.TextInput(
                                      attrs={'class': 'form-control',
                                             'aria-label': 'To Do',
                                             'aria-describedby': 'inputGroup-sizing-default',
                                             'placeholder' : 'description?'}
                                  ) )
