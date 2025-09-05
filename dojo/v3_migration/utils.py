from contextlib import contextmanager
from functools import wraps

from django.shortcuts import redirect
from django.urls import reverse, get_urlconf, set_urlconf, clear_url_caches

from dojo.models import System_Settings


def v3_migration_enabled():
    return System_Settings.objects.get().enable_v3_migration


def redirect_view(to):
    def _redirect(request, **kwargs):
        return redirect(to, **kwargs)
    return _redirect


# add_product_to_product_type => add_asset_to_organization, add_product => add_asset
def v3_migration(**redirect_map):  # redirect_view_name):
    def _decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if request.resolver_match.view_name in redirect_map.values() or not v3_migration_enabled():
                # Can just forward
                return view_func(request, **kwargs)
            # Need to redirect
            redirect_view_name = redirect_map.get(request.resolver_match.view_name)
            return redirect(reverse(redirect_view_name, args=args, kwargs=kwargs))
        return _wrapped
    return _decorator


def get_migration_urlconf_module():
    if v3_migration_enabled():
        return "dojo.v3_migration.urls"
    return "dojo.urls"


@contextmanager
def set_migration_urlconf():
    original_urlconf = get_urlconf()
    try:
        set_urlconf(get_migration_urlconf_module())
        clear_url_caches()
        yield
    finally:
        set_urlconf(original_urlconf)
        clear_url_caches()
