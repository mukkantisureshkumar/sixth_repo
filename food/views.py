from django.shortcuts import render

# Create your views here.
def hott(request):
    return render(request,'hott.html')

def sweet(request):
    return render(request,'sweet.html')