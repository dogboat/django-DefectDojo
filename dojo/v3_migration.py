from django.shortcuts import redirect

from dojo.models import System_Settings


def enable_v3_migration():
    return System_Settings.objects.get().enable_v3_migration


def redirect_view(to):
    def _redirect(request, **kwargs):
        return redirect(to, **kwargs)
    return _redirect

