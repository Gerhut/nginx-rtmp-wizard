from django.apps import AppConfig


class NginxRtmpWizardConfig(AppConfig):
    name = 'nginx_rtmp_wizard'

    def ready(self):
        from . import signals
