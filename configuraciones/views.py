from django.shortcuts import render

# Create your views here.

def configuraciones(request):
    return render(request, 'configuraciones_page.html', {})