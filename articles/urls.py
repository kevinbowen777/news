from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleUpdateView,
    CommentDeleteView,
    CommentDetailView,
    CommentUpdateView,
    article_detail,
    article_list,
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
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:article_id>/share/", article_share, name="article_share"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
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
