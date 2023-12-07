from django.urls import path
from .views import translate_view, saved_texts,save_word_user

urlpatterns = [
    path('', translate_view, name='translate'),
    path('saved_texts/', saved_texts, name='saved_texts'),
]
