from django import forms
from .models import Image, Video, File


# Form for Image Upload
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title1', 'image']


# Form for Video Upload
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title2', 'video']


# Form for File Upload
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['title3', 'file']


# -------------------------------------------------
# forms.py
from django import forms


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(), max_length=255)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), max_length=255)
