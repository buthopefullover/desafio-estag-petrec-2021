from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import os

def index(request):
    return render(request, 'index.html')

def data(request):
    context={}

    print(request.method)

    if request.method =='POST':
        print("socorro")
        print(request.FILES)
        uploadedFile = request.FILES.get('document', False)
        print(uploadedFile)
        if uploadedFile.name.endswith('.csv'):
            saveFile = FileSystemStorage()
            name = saveFile.save(uploadedFile.name, uploadedFile)

            dir = os.getcwd()
            fileDirectory = dir+'\media\\'+name
        else:
            messages.warning(request, 'File was not uploaded. Please use csv file extension!')

    return render(request, 'data.html')

def graph(request):

    
    return render(request, 'graph.html')

def feedback(request):
    return render(request, 'feedback.html')