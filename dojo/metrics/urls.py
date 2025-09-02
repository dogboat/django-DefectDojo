from django.urls import re_path

from dojo.metrics import views
from dojo.v3_migration import redirect_view, v3_migration_enabled

if v3_migration_enabled():
    # References Asset and Organization.
    urlpatterns = [
        #  metrics
        re_path(r"^metrics$", views.metrics, {"mtype": "All"},
                name="metrics"),
        re_path(r"^critical_asset_metrics$", views.critical_product_metrics, {"mtype": "All"},
                name="critical_product_metrics"),
        re_path(r"^metrics/all$", views.metrics, {"mtype": "All"},
                name="metrics_all"),
        re_path(r"^metrics/organization$", views.metrics, {"mtype": "All"},
                name="metrics_product_type"),
        re_path(r"^metrics/simple$", views.simple_metrics,
                name="simple_metrics"),
        re_path(r"^metrics/organization/(?P<mtype>\d+)$",
                views.metrics, name="product_type_metrics"),
        re_path(r"^metrics/organization/counts$",
                views.product_type_counts, name="product_type_counts"),
        re_path(r"^metrics/asset/tag/counts$",
                views.product_tag_counts, name="product_tag_counts"),
        re_path(r"^metrics/engineer$", views.engineer_metrics,
                name="engineer_metrics"),
        re_path(r"^metrics/engineer/(?P<eid>\d+)$", views.view_engineer,
                name="view_engineer"),
        # Backward support; these can be removed after v3 migration is complete.
        re_path(r"^critical_product_metrics$", redirect_view("critical_product_metrics")),
        re_path(r"^metrics/product/type$", redirect_view("metrics_product_type")),
        re_path(r"^metrics/product/type/(?P<mtype>\d+)$", redirect_view("product_type_metrics")),
        re_path(r"^metrics/product/type/counts$", redirect_view("product_type_counts")),
    ]
else:
    # References Product and Product Type. This can be removed after v3 migration is complete.
    urlpatterns = [
        #  metrics
        re_path(r"^metrics$", views.metrics, {"mtype": "All"},
            name="metrics"),
        re_path(r"^critical_product_metrics$", views.critical_product_metrics, {"mtype": "All"},
            name="critical_product_metrics"),
        re_path(r"^metrics/all$", views.metrics, {"mtype": "All"},
            name="metrics_all"),
        re_path(r"^metrics/product/type$", views.metrics, {"mtype": "All"},
            name="metrics_product_type"),
        re_path(r"^metrics/simple$", views.simple_metrics,
            name="simple_metrics"),
        re_path(r"^metrics/product/type/(?P<mtype>\d+)$",
            views.metrics, name="product_type_metrics"),
        re_path(r"^metrics/product/type/counts$",
            views.product_type_counts, name="product_type_counts"),
        re_path(r"^metrics/product/tag/counts$",
            views.product_tag_counts, name="product_tag_counts"),
        re_path(r"^metrics/engineer$", views.engineer_metrics,
            name="engineer_metrics"),
        re_path(r"^metrics/engineer/(?P<eid>\d+)$", views.view_engineer,
            name="view_engineer"),
        # Forward support
        re_path(r"^critical_asset_metrics$", redirect_view("critical_product_metrics")),
        re_path(r"^metrics/organization$", redirect_view("metrics_product_type")),
        re_path(r"^metrics/organization/(?P<mtype>\d+)$", redirect_view("product_type_metrics")),
        re_path(r"^metrics/organization/counts$", redirect_view("product_type_counts")),
    ]
