from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^one$', index_views),
    url(r'^two$',index)

]