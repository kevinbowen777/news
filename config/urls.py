from django.conf import settings  # noqa:F401
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from articles.sitemaps import ArticleSitemap

sitemaps = {
    "articles": ArticleSitemap,
}

urlpatterns = [
    # Django admin
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("resources/", admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("articles/", include("articles.urls")),
    path("accounts/", include("accounts.urls")),
    path("", include("pages.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
if settings.DEBUG:
    import debug_toolbar  # noqa: F401  # pragma: no cover

    urlpatterns = [  # pragma: no cover
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
"""
