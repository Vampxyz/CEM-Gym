from django.shortcuts import render
from gym import models


# Create your views here.
def index(request):
    modalities = models.Modality.objects.filter(active=True)
    classes = models.Class.objects.all()

    context = {
        "modalities": modalities,
        "classes": classes,
    }

    return render(request, "index.html", context)


def classesList(request):
    classes = models.Class.objects.all()

    context = {
        "classes": classes,
    }

    return render(request, "classesList.html", context)
