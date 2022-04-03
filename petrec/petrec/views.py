from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def data(request):
    return render(request, 'data.html')

def graph(request):
    return render(request, 'graph.html')

def feedback(request):
    return render(request, 'feedback.html')