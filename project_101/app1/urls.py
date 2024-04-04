from .import views
from django.urls import path,include


urlpatterns=[path('',views.home,name="home"),
             path('html',views.html,name="HTML_PAGE"),
             path('user_input',views.user_input,name="User_data")
              ]