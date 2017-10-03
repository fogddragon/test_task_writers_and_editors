from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from articles.views import CreateArticleView, UpdateArticleView, ArticleView

urlpatterns = [
    url(r'^create/$', login_required(CreateArticleView.as_view()), name='create_article'),
    url(r'^update/(?P<pk>[-\w]+)/$', login_required(UpdateArticleView.as_view()), name='update_article'),
    url(r'^(?P<pk>[-\w]+)/$', ArticleView.as_view(), name='article'),

]