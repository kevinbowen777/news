from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
    CommentCreateView,
    CommentDeleteView,
    CommentDetailView,
    CommentUpdateView,
    article_share,
)

urlpatterns = [
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:slug>/",
        ArticleDetailView.as_view(),
        name="article_detail",
    ),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("", ArticleListView.as_view(), name="article_list"),
    path("<int:article_id>/share/", article_share, name="article_share"),
    path(
        "<int:pk>/comment/add/",
        CommentCreateView.as_view(),
        name="comment_new",
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
