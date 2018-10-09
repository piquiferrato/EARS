from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('usuarios', views.UsuarioViewSet, base_name = 'usuarios')
router.register('tecnicos', views.TecnicoViewSet, base_name = 'tecnicos')
router.register('pedidos', views.PedidoViewSet, base_name = 'pedidos')
router.register('mispedidos', views.PedidoMiUsuarioSet, base_name = 'mis_pedidos')
router.register('registrar', views.Registrar, base_name = 'registro')
router.register('login', views.LoginView, base_name = 'login')
router.register('logout', views.LogoutView, base_name = 'logout')



urlpatterns = [
    path('', include(router.urls)),
]
