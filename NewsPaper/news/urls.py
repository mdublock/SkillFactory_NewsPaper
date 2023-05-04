from django.urls import path
from .views import (PostsList, PostsDetail, NewsCreate, ArticleCreate,
                    NewsUpdate, ArticleUpdate, NewsDelete, ArticleDelete)
from . import views

urlpatterns = [

    path('', PostsList.as_view()),
    path('<int:pk>', PostsDetail.as_view(), name='news_detail'),
    path('search/', views.post_search, name='news_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('<int:pk>/edit/', ArticleUpdate.as_view(), name='article_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]
