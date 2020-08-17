"""
dip URL Configuration

"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from dip import settings
from dshop.views import IndexView, ArticleView, ArticleDetail

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('dshop/', include('dshop.urls', namespace='dshop')),
    path('articles/', ArticleView.as_view(), name='articles_list'),
    path('articles/<slug>/', ArticleDetail.as_view(), name='articles_detail_url'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
