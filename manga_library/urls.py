from django.urls import path
from . import views

app_name = 'manga_library'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("authors", views.list_data, name="list_data"),
    path("series/<int:author_pk>", views.list_series, name="list_series"),
    path("manga/<int:series_pk>", views.list_manga, name="list_manga")
]