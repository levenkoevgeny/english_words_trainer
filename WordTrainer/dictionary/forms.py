from django.forms import ModelForm
from .models import Dictionary, Word


class DictionaryForm(ModelForm):
    class Meta:
        model = Dictionary
        fields = ['dictionary_name',]


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ['native_meaning', 'foreign_meaning']