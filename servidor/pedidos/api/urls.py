from django.urls import include, path
from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('users/', views.UserListView.as_view()),
    path('users/<int:id>/', views.UniqueUserListView.as_view()),
    path('users/commons/', views.CommonUsersListView.as_view()),
    path('users/technicians/', views.TechniciansListView.as_view()),
    path('types/', views.TypesView.as_view()),
    path('types/<int:id>', views.TypeObjectView.as_view()),
    path('status/', views.StatusView.as_view()),
    path('status/<int:id>', views.StatusObjectView.as_view()),
    path('priority/', views.PriorityView.as_view()),
    path('priority/<int:id>', views.PriorityObjectView.as_view()),
    path('requisitions/', views.RequisitionListView.as_view()),
    path('requisitions/mine/<int:id>/', views.MyRequisitionsListView.as_view()),
    path('requisitions/<int:id>/', views.MyRequisitionsListView.as_view()),
    path('requisitions/update/<int:id>/', views.UpdateRequisitionView.as_view()),
    path('requisitions/delete/<int:id>/', views.DeleteRequisitionView.as_view()),
    path('requisitions/systems/', views.SystemsView.as_view()),
    path('requisitions/systems/<int:id>/', views.UniqueSystemView.as_view()),
    path('requisitions/systems/delete/<int:id>/', views.DeleteSystemView.as_view()),
    path('requisitions/modules/', views.ModulesView.as_view()),
    path('requisitions/modules/<int:id>/', views.UniqueModuleView.as_view()),
    path('requisitions/modules/delete/<int:id>/', views.DeleteModuleView.as_view()),
    path('requisitions/modules/system/<int:id>/', views.SystemModulesView.as_view()),
    path('requisitions/constancys/', views.ConstancysView.as_view()),
    path('requisitions/constancys/<int:id>/', views.UniqueConstancyView.as_view()),
    path('requisitions/constancys/delete/<int:id>/', views.DeleteConstancyView.as_view()),
    path('requisitions/status/<int:id>/', views.RequisitionByStatusView.as_view()),
    path('requisitions/status/<int:id>/order/date/<int:order>/', views.RequisitionByStatusAndDateView.as_view()),
    path('requisitions/status/<int:id>/order/priority/<int:order>/', views.RequisitionByStatusAndPriorityView.as_view()),
    path('requisitions/order/priority/<int:order>', views.OrderRequisitionByPriority.as_view()),
    path('requisitions/order/date/<int:order>', views.OrderRequisitionByDate.as_view()),
    path('requisitions/order/author/<int:order>', views.OrderRequisitionByAuthor.as_view()),
    path('requisitions/underway/technician/<int:id>', views.UnderwayByTechnicianView.as_view()),
    path('requisitions/done/technician/<int:id>', views.ImplementedByTechnicianView.as_view()),
    path('priority/<int:id>/', views.Priority.as_view()),
    path('systems/affected/', views.AffectedSystems.as_view()),
    path('modules/done/<int:system>/', views.SystemAffectedModules.as_view()),
    path('constancys/module/<int:module>', views.ModulesConstancy.as_view()),
]
