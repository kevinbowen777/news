from django.urls import path

from .feeds import LatestArticlesFeed
from .views import (
    article_create,
    article_delete,
    article_detail,
    article_list,
    article_search,
    article_share,
    article_update,
    comment_add,
)

urlpatterns = [
    path("", article_list, name="article_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:article>/",
        article_detail,
        name="article_detail",
    ),
    path("new/", article_create, name="article_new"),
    path("<int:pk>/edit/", article_update, name="article_update"),
    path("<int:article_id>/share/", article_share, name="article_share"),
    path("feed/", LatestArticlesFeed(), name="article_feed"),
    path("search/", article_search, name="article_search"),
    path("<int:pk>/delete/", article_delete, name="article_delete"),
    path("<slug:tag_slug>/", article_list, name="article_list_by_tag"),
    path(
        "<int:article_id>/comment/add/",
        comment_add,
        name="comment_add",
    ),
]
