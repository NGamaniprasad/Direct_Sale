from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Image(models.Model):
    title1 = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  # Store images in 'media/images/'

    def __str__(self):
        return self.title1


# Model for Video
class Video(models.Model):
    title2 = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')  # Store videos in 'media/videos/'

    def __str__(self):
        return self.title2


# Model for File
class File(models.Model):
    title3 = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')  # Store files in 'media/files/'

    def __str__(self):
        return self.title3


class File1(models.Model):
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File uploaded at {self.uploaded_at}"
