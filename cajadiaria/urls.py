from django.conf.urls import include, url
from . import views

urlpatterns=[

    url(r'^$',views.post_list),
    url(r'^accounts/profile/$',views.post_list),
    url(r'^nuevacuenta/$',views.cuenta_nueva,name='cuenta_nueva'),
    url(r'^cuenta/(?P<pk>[0-9]+)/edit/$', views.cuenta_edita, name='cuenta_edita'),
    url(r'^cuenta/(?P<pk>[0-9]+)/$',views.detallecaja,name='detallecaja'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.cuenta_remove, name='cuenta_remove')
]
