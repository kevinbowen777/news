from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Article, Comment


class ArticleListView(ListView):
    queryset = Article.published.all()
    context_object_name = "articles"
    paginate_by = 3
    template_name = "articles/article_list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    context_object_name = "article"
    template_name = "articles/article_detail.html"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "articles/article_new.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    action = "Update"
    template_name = "articles/article_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = "comments/comment_list.html"

    paginate_by = 3


class CommentDetailView(LoginRequiredMixin, DetailView):
    model = Comment
    template_name = "comments/comment_detail.html"


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = (
        "article",
        "comment",
    )
    template_name = "comments/comment_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "comments/comment_delete.html"
    # success_url = reverse_lazy("comment_list")
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "comments/comment_new.html"
    fields = ("article", "comment")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
