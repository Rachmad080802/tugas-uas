from django.db import models

# Create your models here.
class Upload(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images')
    date = models.DateTimeField()
    
    def __str__(self):
        return self.judul
    
class KontakModel(models.Model):
    nama = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    pesan = models.TextField()
