from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.BlogPostListView.as_view(), name='blog'),
    path('blog/<int:pk>', views.BlogPostDetailView.as_view(), name='blog-detail'),
    path('blogger/', views.BloggerListView.as_view(), name='blogger'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
]

