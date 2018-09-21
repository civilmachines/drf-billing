from django.apps import AppConfig


class DRFBillingConfig(AppConfig):
    name = 'drf_billing'
    verbose_name = 'Billing'

    def ready(self):
        from .signals import handlers
