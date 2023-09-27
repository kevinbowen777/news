from django import forms

from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = [
            "title",
            "tags",
            "status",
            "body",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = [
            "name",
            "email",
            "body",
        ]


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class SearchForm(forms.Form):
    query = forms.CharField(
        label="", widget=forms.TextInput(attrs={"placeholder": "Search..."})
    )
