from django.conf.urls import url
from velocity.views import contact
urlpatterns =[
     
    url(r'^contact/$',contact,name="contact")
    ]
