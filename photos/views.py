from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Photo

# Create your views here.


def hello(request):
    return HttpResponse('Hello')


def detail(request, num=1):
    photo = get_object_or_404(Photo, pk=num)

    messages = (
        '<p>{pk} photo is shown</p>'.format(pk=photo.pk),
        '<p>url: {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),
    )
    return HttpResponse('\n'.join(messages))
