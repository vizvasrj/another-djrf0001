from django.urls import path, re_path

from .import views

urlpatterns = [
    path("", views.get_data),
    path("add/", views.add_data),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks/<str:pk>/", views.tasks_detail, name="tasks_detail"),
    re_path(r'^upload/(?P<filename>[^/]+)$', views.FileUploadView.as_view()),
    re_path('^demo/', views.UserListView.as_view()),

]