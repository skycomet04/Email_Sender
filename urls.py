from django.urls import path
from . import views
urlpatterns=[
    path('', views.youtube, name='youtube'),
    path('emailsender',views.emailsender,name='emailsender')
]
