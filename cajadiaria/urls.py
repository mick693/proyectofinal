from django.conf.urls import include, url
from . import views

urlpatterns=[
    url(r'^$',views.post_list),
        #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^nuevacuenta/$',views.cuenta_nueva,name='cuenta_nueva'),
    url(r'^cuenta/(?P<pk>[0-9]+)/$',views.detallecaja,name='detallecaja')
]
