from django.shortcuts import render,redirect, HttpResponse
from .forms import DocumentForm
from .models import Document
import numpy as np
import cv2
import numpy as np


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        global file_path
        file_path = request.FILES['document']
        if form.is_valid():
            form.save()
            return redirect('result')
    else:
        form = DocumentForm()
    return render(request, 'reiwa_app/model_form_upload.html', {
        'form': form
    })

def result(request):
    reiwa_path = cv2.imread("reiwa_app/static/reiwa_app/assets/reiwa.jpg")
    image_path = cv2.imread("media/documents/" + str(file_path))
    reiwa_path = cv2.resize(reiwa_path, (32, 32))
    image_path = cv2.resize(image_path, (32, 32))
    reiwa_path = np.ravel(reiwa_path)
    image_path = np.ravel(image_path)
    similarity = round(1e7 * np.dot(image_path, reiwa_path) / (np.linalg.norm(image_path) * np.linalg.norm(reiwa_path)))
    return render(request, 'reiwa_app/result.html', {
                'data': file_path,
                'similarity': similarity,
                'image_path': image_path,
                'reiwa_path': reiwa_path
            })