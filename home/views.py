from django.shortcuts import render


# Create your views here.
def get_index(request):

    return render(request, 'templates/index.html')

def about(request):
    return render(request, "about.html")

