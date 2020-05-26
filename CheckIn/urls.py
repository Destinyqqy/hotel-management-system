from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index,name='Index'),
    path("scan/", views.ShowScaning, name="ShowScaning"),
    path("personInfo/", views.ShowScanInfo, name="ShowScanInfo"),
    path("personInfo/SplitFlow/", views.SplitFlow, name="SplitFlow"),
    path("SplitFlow/", views.SplitFlow, name="SplitFlow"),
    path("privacyPolicy/<agree>",views.AgreePrivacy,name="AgreePrivacy"),
    path("SelectRoomType/<room_type>[a-z]+)", views.SelectRoomType, name="SelectRoomType"),
    path("SelectLocation/<room_id>)", views.SelectLocation, name="SelectLocation"),
    path("PersonInfo", views.PersonInfo),#####
]
