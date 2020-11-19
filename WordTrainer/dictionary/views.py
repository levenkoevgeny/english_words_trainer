from django.http import JsonResponse
from django.shortcuts import render
from .models import Dictionary, Word
from django.views import View
from .forms import DictionaryForm, WordForm


def dictionary_list(request):
    dictionary_list = Dictionary.objects.filter(owner=request.user)
    return render(request, 'dictionary/dictionary_list.html', {
        'dictionary_list': dictionary_list
    })


class DictionaryAddView(View):
    def get(self, request):
        form = DictionaryForm
        return render(request, 'dictionary/dictionary_input_form.html', {'form': form})

    def post(self, request):
        form = DictionaryForm(request.POST)
        if form.is_valid():
            dictionary = form.save(commit=False)
            dictionary.owner = request.user
            dictionary.save()
            return JsonResponse({'': ''}, safe=False)
        else:
            error_message = "Заполните правильно форму!"
            return JsonResponse({'error': error_message}, safe=False)


class WordAddView(View):
    def get(self, request, dictionary_id):
        form = WordForm
        return render(request, 'dictionary/word/word_input_form.html', {
            'form': form,
            'dictionary_id': dictionary_id,
        })

    def post(self, request, dictionary_id):
        form = WordForm(request.POST)
        if form.is_valid():
            new_word = form.save(commit=False)
            new_word.dictionary = Dictionary.objects.get(pk=dictionary_id)
            new_word.save()
            return JsonResponse({'': ''}, safe=False)
        else:
            error_message = "Заполните правильно форму!"
            return JsonResponse({'error': error_message}, safe=False)


class TrainingView(View):
    def get(self, request, dictionary_id):
        return render(request, 'dictionary/training.html', {
            'dictionary_id': dictionary_id,
        })


def word_list(request, dictionary_id):
    dictionary_word_list = Word.objects.filter(dictionary_id=dictionary_id)
    return render(request, 'dictionary/word/word_list.html', {
        'dictionary_word_list': dictionary_word_list,
        'dictionary_id': dictionary_id,
    })
