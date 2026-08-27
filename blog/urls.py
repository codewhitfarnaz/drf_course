from django.urls import path
from django.contrib import admin
from .import views

urlpatterns=[
    path('blog',views.hello_world),
    path('blog/cbv',views.HelloWorld.as_view()),
    path('articles/',views.ArticleListView.as_view()),
    path('articles/<int:pk>',views.ArticleDetailSerializer.as_view()),
    path('articles/add',views.AddArticleView.as_view()),
    path('article/update/<int:pk>',views.ArticleUpdateView.as_view()),
]