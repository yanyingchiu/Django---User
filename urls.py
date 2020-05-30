# path: mysite / mysite / urls.py

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from trips.views import home, post_detail, post_new, post_edit, post_delete, showImg, register
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    re_path(r'^post/(?P<pk>\d+)/$', post_detail, name="post_detail"),
    re_path(r'^post/new/$', post_new, name='post_new'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'),
    re_path(r'^post/(?P<pk>[0-9]+)/delete/$', post_delete, name='post_delete'),

    
    path('showImg/', showImg)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
