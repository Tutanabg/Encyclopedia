from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("" , views.index, name="index"),
    path("choose/" , views.choose, name="choose"),
    path("new/" , views.new, name="new"),
    path("add/" , views.add, name="add"),
    path("search/" , views.search, name="search"),
    path("error/" , views.error, name="error"),
    path("empty/" , views.empty, name="empty"),
    path("wiki/<str:title>/",views.entry, name="entry"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
    
]



