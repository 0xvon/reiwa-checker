from django.db import models
 
class Document(models.Model):
    document = models.FileField(upload_to='documents/', verbose_name='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='documents/', default='defo')
