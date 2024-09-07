import os
from django.shortcuts import render
from django.conf import settings
from .forms import MediaUploadForm
from .selenium_script import upload_and_search_image

def media_upload(request):
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_path = os.path.join('media/images', image.name)
            with open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            
            # Call the Selenium script for image
            search_results = upload_and_search_image(image_path)
            return render(request, 'similar/index.html', {'form': form,'results': search_results})
    else:
        form = MediaUploadForm()
    
    return render(request, 'similar/index.html', {'form': form})
