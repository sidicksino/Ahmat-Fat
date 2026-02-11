from django.shortcuts import render

def loading_view(request):
    return render(request, 'Myapp/loading.html')
