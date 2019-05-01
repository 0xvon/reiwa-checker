from django.shortcuts import render,redirect, HttpResponse
from .forms import DocumentForm
from .models import Document
from reiwa_prj import settings
from django.core.cache import cache
from django.views.decorators.cache import never_cache
import numpy as np
import cv2
import os
import time


def model_form_upload(request):
    cache.clear()
    global input_path
    global form

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        input_path = settings.MEDIA_URL + "documents/" + str(request.FILES['photo'])
        if form.is_valid():
            form.save()
            form = DocumentForm()
            time.sleep(3)
            return redirect('calc')
    else:
        form = DocumentForm()
    return render(request, 'reiwa_app/model_form_upload.html', {
        'form': form,
    })

def calc(request):
    time.sleep(2)
    global reiwa_path
    reiwa_path = cv2.imread("reiwa_app/static/reiwa_app/assets/reiwa.jpg", 0)
    global image_path
    image_path = cv2.imread(input_path, 0)
    reiwa_path = cv2.resize(reiwa_path, (100, 100))
    image_path = cv2.resize(image_path, (100, 100))
    reiwa_path = np.ravel(reiwa_path)
    image_path = np.ravel(image_path)
    global similarity
    similarity = round(1e7 * np.dot(image_path, reiwa_path) / (np.linalg.norm(image_path) * np.linalg.norm(reiwa_path)))
    eucrid_distance = np.linalg.norm(np.abs(reiwa_path - image_path), ord=2)
    if eucrid_distance < 1:
        similarity = 100.0
    elif eucrid_distance < 10:
        similarity = 80.0
    elif eucrid_distance < 100:
        similarity = 60.0
    elif eucrid_distance < 300:
        similarity = 50.0
    
    time.sleep(2)
    return redirect('result')

def result(request):
    if request.method == 'POST':
        os.remove(input_path)
        return redirect('upload')
    
    return render(request, 'reiwa_app/result.html', {
                'data': input_path,
                'similarity': similarity
            })
    
