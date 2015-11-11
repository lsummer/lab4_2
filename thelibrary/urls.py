"""thelibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from books.views import intr,noauthor,full,books_insert,author_insert,search_books,Delete,update,main,search

urlpatterns = [
    url(r'^books_insert/$', books_insert),
    url(r'^author_insert/$', author_insert),
    #url(r'^search_books/$', search_books),
    url(r'^search/$', search),
    url(r'^search_result/$', search_books),
    url(r'^delete/$',Delete),
    url(r'^update/$', update),
    url(r'^fullinformation/$', full),
    url(r'^noauthor/$',noauthor),
    url(r'^intr/$',intr),
    url('', main),
]
