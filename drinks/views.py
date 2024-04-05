from django.shortcuts import render

# Create your views here.
def teachers(request):
    return render(request,'teachers.html')

def redwine(request):
    return render(request,'redwine.html')
