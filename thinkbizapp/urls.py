from django.urls import path
from . import views


urlpatterns = [
    path('educator',views.educator,name='educator'),
    path('educator/<int:id>',views.educator,name='educator'),
]