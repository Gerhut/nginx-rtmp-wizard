from django.shortcuts import render

from . import models

# Create your views here.
def rtmp_conf(request):
    servers = models.Server.objects.all()
    return render(request, 'rtmp.conf', { 'servers': servers }, content_type='text/plain')
