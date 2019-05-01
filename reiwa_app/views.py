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
import numpy as np


def model_form_upload(request):
    cache.clear()
    global input_path
    global form
    # shutil.rmtree('media/documents')
    # os.mkdir('media/documents')
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        # max_id = Document.objects.latest('id').id
        # obj = Document.objects.get(id=0)
        # input_path = settings.BASE_DIR + obj.photo.url
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
    while input_path is False:
        time.sleep(0.1)

    reiwa_path = cv2.imread("reiwa_app/static/reiwa_app/assets/reiwa.jpg")
    image_path = cv2.imread(input_path)
    while image_path is False:
        time.sleep(0.1)

    reiwa_path = cv2.resize(reiwa_path, (32, 32))
    image_path = cv2.resize(image_path, (32, 32))
    reiwa_path = np.ravel(reiwa_path)
    image_path = np.ravel(image_path)
    global similarity
    similarity = round(1e7 * np.dot(image_path, reiwa_path) / (np.linalg.norm(image_path) * np.linalg.norm(reiwa_path)))
    while similarity is False:
        time.sleep(0.1)
    return redirect('result')
    # return render(request, 'reiwa_app/model_form_upload.html', {
    #     'form': form,
    #     'path': input_path
    # })
    

def result(request):
    if request.method == 'POST':
        os.remove(input_path)
        return redirect('upload')
    
    
    while input_path is False or similarity is False:
        time.sleep(0.1)
        
    return render(request, 'reiwa_app/result.html', {
                'data': input_path,
                'similarity': similarity,
            })
    
