from django.shortcuts import render

# Create your views here.

def dropRocket(request):
  return render(request, "./index.html")