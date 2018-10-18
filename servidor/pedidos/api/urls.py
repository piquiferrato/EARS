from django.urls import include, path
from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('users/', views.UserListView.as_view()),
    path('users/<int:id>/', views.UniqueUserListView.as_view()),
    path('requisitions/', views.RequisitionListView.as_view()),
    path('requisitions/<int:id>/', views.MyRequisitionsListView.as_view()),
    path('requisitions/update/<int:id>/', views.UpdateRequisitionView.as_view()),
    path('requisitions/delete/<int:id>/', views.DeleteRequisitionView.as_view()),
    path('requisitions/systems', views.SystemsView.as_view()),
    path('requisitions/modules', views.ModulesView.as_view()),
]
