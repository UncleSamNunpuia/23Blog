from django.shortcuts import render
# added
from django.http import HttpResponse
from .models import MyModel
# Create your views here.


def home(request):
    # my_object = MyModel.objects.get()
    my_object = MyModel.objects.first()
    my_file_url = my_object.my_file.url
    my_image_url = my_object.my_image.url
    return render(request, 'site_home.html', {'my_obj': my_object})


def tt_home(request):
    return render(request, 'tt_home.html', {})

    # my_object = MyModel.objects.get(id=1)
    # my_file_url = my_object.my_file.url
    # my_image_url = my_object.my_image.url
