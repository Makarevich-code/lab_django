from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def how_to_find(request):
    return render(request, 'how_to_find.html')

def poster(request):
    return render(request, 'poster.html')

def troupe(request):
    return render(request, 'troupe.html')
