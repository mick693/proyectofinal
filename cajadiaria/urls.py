from django.conf.urls import include, url
from . import views

urlpatterns=[

    url(r'^$',views.post_list),
    url(r'^accounts/profile/$',views.post_list),
    url(r'^nuevacuenta/$',views.cuenta_nueva,name='cuenta_nueva'),
    url(r'^cuenta/(?P<pk>[0-9]+)/$',views.detallecaja,name='detallecaja')
]
