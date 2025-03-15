from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore


# Create your views here.
def index(request):
    return render(request, "index.html")


def counter(request):
    text = request.GET["text"]
    return render(request, "counter.html")
