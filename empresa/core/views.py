from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "core/home.html")


def about(requets):
    return render(requets, "core/about.html")

def store(request):
    return  render(request, "core/store.html")
