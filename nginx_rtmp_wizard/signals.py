from django.conf import settings
from django.db.models import signals
from django.dispatch import receiver
from django.template.loader import get_template

from os import system

from . import models

@receiver(
    [signals.post_save, signals.post_delete],
    sender=models.Server,
    dispatch_uid='configure_nginx_Server')
@receiver(
    [signals.post_save, signals.post_delete],
    sender=models.Application,
    dispatch_uid='configure_nginx_Application')
@receiver(
    [signals.post_save, signals.post_delete],
    sender=models.Push,
    dispatch_uid='configure_nginx_Push')
def configure_nginx(sender, **kwargs):
    servers = models.Server.objects.all()
    rtmp_conf = get_template('rtmp.conf').render({ 'servers': servers })
    with open(settings.RTMP_CONF, 'w') as f:
        f.write(rtmp_conf)
    system('nginx -s reload')
