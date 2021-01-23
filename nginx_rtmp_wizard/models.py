from django.conf import settings
from django.core import validators
from django.db import models

DEFAULT_RTMP_PORT = 1935


class Server(models.Model):
    listen = models.PositiveIntegerField(
        default=DEFAULT_RTMP_PORT,
        unique=True,
        validators=[
            validators.MinValueValidator(1024),
            validators.MaxValueValidator(65535)
        ])

    def __str__(self):
        if self.listen == DEFAULT_RTMP_PORT:
            return 'rtmp://{}'.format(settings.RTMP_HOSTNAME)
        else:
            return 'rtmp://{}:{}'.format(settings.RTMP_HOSTNAME, self.listen)


class Application(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    name = models.SlugField(default='live')
    live = models.BooleanField(default=False)

    def __str__(self):
        return '{}/{}'.format(self.server, self.name)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['server', 'name'],
                name='unique_server_application_name')]


class Push(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    url = models.CharField(
        max_length=255,
        unique=True,
        validators=[
            validators.URLValidator(schemes=['rtmp'])
        ])

    def __str__(self):
        return 'push {};'.format(self.url)
