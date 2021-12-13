from django.conf.urls import url
from .views import *

# urlpatterns=[
#
#     url(r'^show_Actiune$',show_Actions,name='show_Actions'),
#
# ]

urlpatterns =[

    url(r'^$', display , name='display'),
    url(r'^show_Actiune$',show_Actions,name='show_Actions'),
    url(r'^show_Horror$',show_Horrors,name='show_Horrors'),
    url(r'^show_Comedie$',show_Comedies,name='show_Comedies'),
    url(r'^show_Drama$',show_Dramas,name='show_Dramas'),
    url(r'^New_Actiunes$',New_Actiune,name='New_Actiune'),
    url(r'^New_Horrors$',New_Horror,name='New_Horror'),
    url(r'^New_Comedies$',New_Comedie,name='New_Comedie'),
    url(r'^New_Dramas$',New_Drama,name='New_Drama'),
    url(r'^Remove_actiune/(?P<pk>\d+)$',Remove_actiune,name='Remove_actiune'),
    url(r'^Remove_horror/(?P<pk>\d+)$',Remove_horror,name='Remove_horror'),
    url(r'^Remove_drame/(?P<pk>\d+)$',Remove_drame,name='Remove_drame'),
    url(r'^Remove_comedie/(?P<pk>\d+)$',Remove_comedie,name='Remove_comedie'),




]