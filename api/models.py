from django.db import models

# Create your models here.
STATE_CHOICE = ((
    ('Gujrat', 'Gujrat'),
    ('Bihar', 'Bihar'),
    ('UP', 'UP'),
    ('MP', 'MP'),
))


class Profile(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='pimages', blank=True)
    rdoc = models.FileField(upload_to='rdocs', blank=True)
