from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('users/', views.UserListView.as_view()),
]