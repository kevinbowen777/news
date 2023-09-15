from django.urls import path

from .feeds import LatestArticlesFeed
from .views import (
    ArticleDeleteView,
    ArticleUpdateView,
    CommentDeleteView,
    CommentDetailView,
    CommentUpdateView,
    article_create,
    article_detail,
    article_list,
    article_search,
    article_share,
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
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:article_id>/share/", article_share, name="article_share"),
    path("feed/", LatestArticlesFeed(), name="article_feed"),
    path("search/", article_search, name="article_search"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("<slug:tag_slug>/", article_list, name="article_list_by_tag"),
    path(
        "<int:article_id>/comment/add/",
        comment_add,
        name="comment_add",
    ),
    path(
        "comment/<int:pk>/detail/",
        CommentDetailView.as_view(),
        name="comment_detail",
    ),
    path(
        "comment/<int:pk>/delete/",
        CommentDeleteView.as_view(),
        name="comment_delete",
    ),
    path(
        "comment/<int:pk>/edit/",
        CommentUpdateView.as_view(),
        name="comment_edit",
    ),
]
