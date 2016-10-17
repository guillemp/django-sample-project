from django.conf.urls import include, url
from django.contrib import admin
from main import views

""" examples
url(r'^cart/(?P<pk>[0-9]+)/delete/$', views.cart_delete, name='cart_delete'),
url(r'^forum/(?P<slug>[a-zA-Z0-9-]+)$', views.forum_view, name='forum_view'),
url(r'^topic/(?P<slug>[a-zA-Z0-9-._]+)$', views.topic_view, name='topic_view'),
url(r'^recover/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)$', views.recover_confirm_view, name='recover_confirm_view'),
"""

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
]
