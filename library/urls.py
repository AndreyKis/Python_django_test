from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'auth/', views.get_auth, name='get_auth'),
    url(r'books/', views.index, name='index'),
    # ex: /templates/5/
    url(r'books/^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /templates/5/results/
    url(r'books/^(?P<book_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /templates/5/vote/
    url(r'books/^(?P<book_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
