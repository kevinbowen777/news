from typing import ClassVar

from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = ["title", "slug", "author", "publish", "status"]
    list_filter: ClassVar[list[str]] = ["status", "created", "publish", "author"]
    search_fields: ClassVar[list[str]] = ["title", "body"]
    prepopulated_fields: ClassVar[dict[str, tuple]] = {"slug": ("title",)}
    raw_id_fields: ClassVar[list[str]] = ["author"]
    date_hierarchy = "publish"
    ordering: ClassVar[list[str]] = ["status", "publish"]
    inlines: ClassVar[list] = [
        CommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display: ClassVar[list[str]] = [
        "name",
        "email",
        "article",
        "created",
        "active",
    ]
    list_filter: ClassVar[list[str]] = ["active", "created", "updated"]
    search_fields: ClassVar[list[str]] = ["name", "email", "body"]
