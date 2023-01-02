from django.shortcuts import render

# Create your views here.
def h1(request):
    d={'a':100,'b':20}
    return render(request,'h1.html',d)
