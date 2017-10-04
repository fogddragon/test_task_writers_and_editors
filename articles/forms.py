from django import forms

from articles.models import Article


class ArticleForm(forms.ModelForm):
    to_review = forms.BooleanField(required=False)
    reviewed = forms.BooleanField(required=False)

    class Meta:
        model = Article
        fields = ['name', 'link_to_article']

    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()
        if cleaned_data.get('to_review') \
                and self.instance.status != Article.NEW \
                and not cleaned_data.get('link_to_article'):
            self.add_error("link_to_article", 'You cant send article to reviw without link.')
        if cleaned_data.get('reviewed') \
                and self.instance.status != Article.TO_REVIEW:
            self.add_error(None, 'You cant review this article.')
        return cleaned_data

    def save(self, commit=True):
        if self.cleaned_data.get('to_review'):
            self.instance.status = Article.TO_REVIEW
        elif self.cleaned_data.get('reviewed'):
            self.instance.status = Article.REVIEWED
        super(ArticleForm, self).save(commit)