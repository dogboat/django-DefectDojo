from dojo.v3_migration import v3_migration_enabled


class V3MigrationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def get_urlconf(self):
        if v3_migration_enabled():
            return "dojo.urls"
        return "dojo.v3_migration.urls"

    def __call__(self, request):
        request.urlconf = self.get_urlconf()
        return self.get_response(request)
