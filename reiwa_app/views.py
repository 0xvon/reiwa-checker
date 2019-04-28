from django.shortcuts import render,redirect, HttpResponse
from .forms import DocumentForm
from .models import Document


def index(request):
    return HttpResponse('hello')
 

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'reiwa_app/model_form_upload.html', {
        'form': form
    })
