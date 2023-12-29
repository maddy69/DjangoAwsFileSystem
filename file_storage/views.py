from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import File

def file_list(request):
    files = File.objects.all()
    if not files:
        message = 'No Files Available'
    else:
        message = None
    return render(request, 'file_storage/file_list.html', {'files' : files, 'message' : message})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            description = form.cleaned_data.get('description', '')
            File.objects.create(file=uploaded_file, description=description)
            return redirect('file_list')
    else:
        form = UploadFileForm()

    return render(request, 'upload_file.html', {'form':form})