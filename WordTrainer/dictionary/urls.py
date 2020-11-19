from django.urls import path
from . import views

app_name = 'dictionary'

urlpatterns = [
    path('', views.dictionary_list, name='list'),
    path('add/', views.DictionaryAddView.as_view(), name='dictionary_add'),
    path('<dictionary_id>/words', views.word_list, name='dictionary_word_list'),
    path('<dictionary_id>/words/add/', views.WordAddView.as_view(), name='dictionary_word_add'),
    path('<dictionary_id>/words/training/', views.TrainingView.as_view(), name='dictionary_words_training'),

]