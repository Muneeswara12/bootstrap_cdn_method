from django.shortcuts import render

# Create your views here.
def muni(request):
    return render(request,'bootstrap_cdn.html')