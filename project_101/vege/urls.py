from .import views 
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns=[path('',views.vege,name="vege"),
             path('/<int:id>',views.delete,name="delete"),
             path('update/<id>/',views.Update_receipe,name="Update_receipe"),
             
             
              ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
