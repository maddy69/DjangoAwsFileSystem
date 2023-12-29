from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    description = models.TextField()

# views.py

from django.shortcuts import render, redirect
from .models import File

def file_list(request):
    files = File.objects.all()
    return render(request, 'file_list.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'upload_file.html', {'form': form})
