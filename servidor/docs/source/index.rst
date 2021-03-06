.. EARS documentation master file, created by
   sphinx-quickstart on Thu Oct 18 09:49:39 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to EARS's documentation!
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Documentation for the Code
**************************
.. toctree::
   :maxdepth: 2
   :caption: Contents:

pedidos/api models
==================
.. automodule:: pedidos.api.admin
   :members:

pedidos/api apps
================
.. automodule:: pedidos.api.apps
   :members:

pedidos/api forms
=================
.. automodule:: pedidos.api.forms
   :members:

pedidos/api models
==================
.. automodule:: pedidos.api.models
   :members:

pedidos/api serializers
=======================
.. automodule:: pedidos.api.serializers
   :members:

pedidos/api urls
================
.. automodule:: pedidos.api.urls
   :members:
    
path('rest-auth/', include('rest_auth.urls')),

path('users/', views.UserListView.as_view()),
   
path('users/<int:id>/', views.UniqueUserListView.as_view()),
    
path('types/', views.TypesView.as_view()),
    
path('types/<int:id>', views.TypeObjectView.as_view()),
    
path('status/', views.StatusView.as_view()),
    
path('status/<int:id>', views.StatusObjectView.as_view()),
    
path('priority/', views.PriorityView.as_view()),
    
path('priority/<int:id>', views.PriorityObjectView.as_view()),
    
path('requisitions/', views.RequisitionListView.as_view()),
    
path('requisitions/mine/<int:id>/', views.MyRequisitionsListView.as_view()),
    
path('requisitions/technician/<int:id>', views.TechnicianRequisitionView.as_view()),
    
path('requisitions/<int:id>/', views.MyRequisitionsListView.as_view()),
    
path('requisitions/update/<int:id>/', views.UpdateRequisitionView.as_view()),
    
path('requisitions/delete/<int:id>/', views.DeleteRequisitionView.as_view()),
    
path('requisitions/systems/', views.SystemsView.as_view()),
    
path('requisitions/systems/<int:id>/', views.UniqueSystemView.as_view()),
    
path('requisitions/systems/delete/<int:id>/', views.DeleteSystemView.as_view()),
    
path('requisitions/modules/', views.ModulesView.as_view()),
    
path('requisitions/status/waiting/', views.WaitingRequistionsView.as_view()),
    
path('requisitions/status/inprogress/', views.InProgressRequistionsView.as_view()),
    
path('requisitions/status/cancelled/', views.CancelledRequistionsView.as_view()),
    
path('requisitions/status/done/', views.DoneRequistionsView.as_view()),
    
path('requisitions/modules/<int:id>/', views.UniqueModuleView.as_view()),
    
path('requisitions/modules/delete/<int:id>/', views.DeleteModuleView.as_view()),
    
path('requisitions/modules/system/<int:id>/', views.SystemModulesView.as_view()),
    
path('requisitions/constancys/', views.ConstancysView.as_view()),
    
path('requisitions/constancys/<int:id>/', views.UniqueConstancyView.as_view()),
    
path('requisitions/constancys/delete/<int:id>/', views.DeleteConstancyView.as_view()),
    
path('requisitions/status/<int:id>/', views.RequisitionByStatusView.as_view()),
    
path('requisitions/status/<int:id>/order/date/<int:order>/', views.RequisitionByStatusAndDateView.as_view()),
    
path('requisitions/status/<int:id>/order/priority/<int:order>/', views.RequisitionByStatusAndPriorityView.as_view()),
    
path('requisitions/inprogress/technician/<int:id>', views.UnderwayByTechnicianView.as_view()),
    
path('requisitions/done/technician/<int:id>', views.ImplementedByTechnicianView.as_view()),
    
path('priority/<int:id>/', views.Priority.as_view()),
    
path('modules/done/<int:system>/', views.SystemAffectedModules.as_view()),
    
path('constancys/module/<int:module>', views.ModulesConstancy.as_view()),
    
path('search/priority/system/<int:system>/status/<int:status>/order/<int:order>/', views.PriorityAdvancedSearchSystem.as_view()),
    
path('search/date/system/<int:system>/status/<int:status>/order/<int:order>/', views.DateAdvancedSearchSystem.as_view()),
    
path('search/priority/module/<int:module>/status/<int:status>/order/<int:order>/', views.PriorityAdvancedSearchModule.as_view()),
    
path('search/date/module/<int:module>/status/<int:status>/order/<int:order>/', views.DateAdvancedSearchModule.as_view()),
    
path('search/priority/technician/<int:technician>/status/<int:status>/order/<int:order>/', views.PriorityAdvancedSearchTechnician.as_view()),
    
path('search/date/technician/<int:technician>/status/<int:status>/order/<int:order>/', views.DateAdvancedSearchTechnician.as_view()),

