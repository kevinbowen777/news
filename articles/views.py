from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView, UpdateView
from taggit.models import Tag

from .forms import ArticleForm, CommentForm, EmailPostForm, SearchForm
from .models import Article, Comment


@login_required
def article_create(request):
    template_name = "articles/article_new.html"
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.instance.author = request.user
        form.save()
        return redirect("article_list")

    return render(request, template_name, {"form": form})


"""
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "articles/article_new.html"
    fields = ["title", "tags", "status", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
"""


def article_list(request, tag_slug=None):
    article_list = Article.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        article_list = article_list.filter(tags__in=[tag])
    paginator = Paginator(article_list, 3)
    page_number = request.GET.get("page", 1)
    try:
        articles = paginator = paginator.page(page_number)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(
        request, "articles/article_list.html", {"articles": articles, "tag": tag}
    )


def article_detail(request, year, month, day, article):
    article = get_object_or_404(
        Article,
        status=Article.Status.PUBLISHED,
        slug=article,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    comments = article.comments.filter(active=True)
    form = CommentForm()

    article_tags_ids = article.tags.values_list("id", flat=True)
    similar_articles = Article.published.filter(tags__in=article_tags_ids).exclude(
        id=article.id
    )
    similar_articles = similar_articles.annotate(same_tags=Count("tags")).order_by(
        "-same_tags", "-publish"
    )[:4]

    return render(
        request,
        "articles/article_detail.html",
        {
            "article": article,
            "comments": comments,
            "form": form,
            "similar_articles": similar_articles,
        },
    )


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = (
        "title",
        "status",
        "tags",
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


def article_share(request, article_id):
    article = get_object_or_404(Article, id=article_id, status=Article.Status.PUBLISHED)
    sent = False

    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            article_url = request.build_absolute_uri(article.get_absolute_url())
            subject = f"{cd['name']} recommends you read " f"{article.title}"
            message = (
                f"Read {article.title} at {article_url}\n\n"
                f"{cd['name']}'s comments: {cd['comments']}"
            )
            send_mail(subject, message, "kevin.bowen@gmail.com", [cd["to"]])
            sent = True

    else:
        form = EmailPostForm()
    return render(
        request,
        "articles/article_share.html",
        {"article": article, "form": form, "sent": sent},
    )


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
        "body",
    )
    template_name = "comments/comment_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.name == self.request.user


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "comments/comment_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.name == self.request.user


def article_search(request):
    form = SearchForm()
    query = None
    results = []

    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            search_vector = SearchVector("title", weight="A") + SearchVector(
                "body", weight="B"
            )
            search_query = SearchQuery(query)
            results = (
                Article.published.annotate(
                    search=search_vector, rank=SearchRank(search_vector, search_query)
                )
                .filter(rank__gte=0.2)
                .order_by("-rank")
            )

    return render(
        request,
        "articles/search.html",
        {
            "form": form,
            "query": query,
            "results": results,
        },
    )


@require_POST
def comment_add(request, article_id):
    article = get_object_or_404(Article, id=article_id, status=Article.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
    return render(
        request,
        "comments/comment_add.html",
        {"article": article, "form": form, "comment": comment},
    )
