from django.conf.urls import include, url
from . import views

urlpatterns=[
    url(r'^$',views.post_list),
    url(r'^nuevacuenta/$',views.cuenta_nueva,name='cuenta_nueva'),
]
