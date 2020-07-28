from django.http import HttpResponse
from django.shortcuts import render
from .forms import MessaggioModelForm

# Create your views here.

def contactView(request):
    if request.method == "POST":
        form = MessaggioModelForm(request.POST)
        if form.is_valid():
            nuovo_messaggio = form.save()
            return HttpResponse ("Messaggio inviato")
    else:
        form = MessaggioModelForm()
    context = {"form":form}
    return render(request, "form/form_contatto.html", context)
