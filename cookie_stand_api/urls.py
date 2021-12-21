from django.urls import path
from . import views

from django.conf.global_settings import *

urlpatterns = [
    path("", views.CookieStandList.as_view(), name="cookieStand_list"),
    path("<int:pk>/", views.CookieStandDetail.as_view(), name="cookieStand_detail"),

    #### NOT WORKING YET
    path("token/verify/", views.verify_token, name="Verify_Token"),

]
