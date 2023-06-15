import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy

from .models import Article


class LatestArticlesFeed(Feed):
    title = "news"
    link = reverse_lazy("article_list")
    description = "Lil' Bits o'News just for you"

    def items(self):
        return Article.published.all()[:7]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        return item.publish
