from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('users/', views.UserListView.as_view()),
    path('users/<int:id>/', views.UniqueUserListView.as_view()),
    path('requisitions/', views.RequisitionListView.as_view()),
    path('requisitions/errors/', views.ErrorsListView.as_view()),
    path('requisitions/requeriments/', views.RequerimentsListView.as_view()),
    path('requisitions/<int:id>/', views.RequisitionsListView2.as_view()),
]