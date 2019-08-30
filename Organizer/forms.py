
from django import forms
from django.core import validators


def check_for_z(value):
    i=0
    if value[i].lower() != 'z':
        raise forms.ValidationError("Erros")


class FormName(forms.ModelForm):

    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()

        email = all_clean_data['email']
        text = all_clean_data['text']

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']

        if len(botcatcher) > 0:
            raise forms.ValidationError('GOTCHA BOT')
