from django.shortcuts import render  # type: ignore
from django.http import HttpResponse  # type: ignore
from .models import Feature


# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.name = "Fast"
    feature1.is_true = True
    feature1.details = "Our service is very quick"
    
    feature2 = Feature()
    feature2.id = 2
    feature2.name = "Yoyo"
    feature2.is_true = False
    feature2.details = "Our service is very quick"
    
    feature3 = Feature()
    feature3.id = 3
    feature3.name = "Easy to Use"
    feature3.is_true = True
    feature3.details = "Our service is very quick"
    
    feature4 = Feature()
    feature4.id = 4
    feature4.name = "Affordable"
    feature4.is_true = False
    feature4.details = "Our service is very quick"
    
    feature5 = Feature()
    feature5.id = 5
    feature5.name = "Trustworthy"
    feature5.is_true = True
    feature5.details = "Our service is very trusty"
    
    features = [feature1, feature2, feature3, feature4, feature5]
    return render(request, "index.html", {"features": features})


def counter(request):
    text = request.POST["text"]
    count_of_words = len(text.split())
    return render(request, "counter.html", {"count": count_of_words})
