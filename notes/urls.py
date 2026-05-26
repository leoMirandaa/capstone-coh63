from django.urls import path

from . import views


urlpatterns = [
    path("", views.NoteListView.as_view(), name="notes_list"),
    path("create/", views.NoteCreateView.as_view(), name="notes_create"),
]
