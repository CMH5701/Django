from django.shortcuts import render
from .models import Main
# Create your views here.
def main(request):
    mains = Main.objects
    return render(request, 'main.html', {'mains':mains})