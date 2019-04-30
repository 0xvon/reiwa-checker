from django.shortcuts import render,redirect, HttpResponse
from .forms import DocumentForm
from .models import Document, Result
import numpy as np
from repository.api import *
import cv2


# global data


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        global data
        data = request.POST.get()
        print(form)
        if form.is_valid():
            form.save()
            return redirect('result')
    else:
        form = DocumentForm()
    return render(request, 'reiwa_app/model_form_upload.html', {
        'form': form
    })

def show_result(request):
    a = np.random.rand(1)
    return render(request, 'reiwa_app/result.html', {
        'data': data
    })