from django.db import models
from django.core.validators import FileExtensionValidator

 
class Document(models.Model):
    document = models.FileField(upload_to='documents/', verbose_name='', validators=[FileExtensionValidator(['png', 'jpeg', 'PNG', 'jpg', 'tif', 'tiff', 'bmp'])],)
    photo = models.ImageField(upload_to='documents/', default='defo', verbose_name='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
