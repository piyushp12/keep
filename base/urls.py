from django.urls import path 
from.import views 

urlpatterns = [
    path('',views.index,name='home'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('Home/',views.Home,name='Home'),
    path('Html/',views.Html,name='Html'),
    path('datascience/',views.datascience,name='datascience')

]
