from django.shortcuts import render, redirect
import translators as ts
from .models import Translation


def translate_view(request):
    text,translate = 'Привет!',''
    if request.method == 'POST':
        text = request.POST.get('text')
        translate = ts.translate_text(text, to_language='zh')
        save_word_user(request, text, translate)
    return render(request, 'translate/translate.html', {'text': translate, 'base_text': text })


def save_word_user(request, text, translate):
    Translation.objects.create(user=request.user, text=text, result=translate)
    return redirect('/translate/')

def saved_texts(request):
    texts = Translation.objects.filter(user=request.user).order_by('-date')
    return render(request, 'translate/saved_texts.html', {'texts': texts})
