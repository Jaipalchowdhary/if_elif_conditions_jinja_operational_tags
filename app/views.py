from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'a':200,'b':300,'c':500}
    return render(request,'ifelif.html',d)

def ifelif (request):
    d={'a':200,'b':300,'c':500}
    return render(request,'ifelif.html',d)
