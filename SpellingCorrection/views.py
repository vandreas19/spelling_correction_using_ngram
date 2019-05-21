from django.shortcuts import render
from django.shortcuts import HttpResponse
from SpellingCorrection.implementasi import spell_correct
# Create your views here.

def ok(request):
    if request.method == 'POST':
        text = request.POST['input']
        res = spell_correct.main(text)
        cont = {'text' : res}
        return render(request,"colorlib-search-3/hasil.html", cont)
    return render(request,"colorlib-search-3/index.html")

def ngram(request):
    w = spell_correct.indexing()
    co = {'index': w}
    return render(request, "colorlib-search-3/my_index.html", co)
    