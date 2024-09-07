from django import forms

class MediaUploadForm(forms.Form):
    image = forms.ImageField(label='Upload an Image')
