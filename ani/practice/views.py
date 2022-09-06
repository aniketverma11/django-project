from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def exersice(request):
    return render(request, 'practice.html')

def practice(request):
    text = request.POST['text']
    length = len(text.split())
    return render(request, "practice2.html", {'length':length})