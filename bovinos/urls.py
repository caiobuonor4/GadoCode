from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Páginas Públicas
    path('', views.landing_page, name='landing'),
    
    # Autenticação (Login/Logout/Registro)
    path('login/', auth_views.LoginView.as_view(template_name='bovinos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', views.registro, name='registro'),

    # Sistema (Protegido)
    path('app/', views.dashboard, name='dashboard'),
    path('cadastro/', views.cadastrar_boi, name='cadastro_boi'),
    path('boi/<uuid:id>/', views.perfil_boi, name='perfil_boi'),
    path('boi/<uuid:id>/', views.perfil_boi, name='perfil_boi'),
    path('boi/<uuid:id>/editar/', views.editar_boi, name='editar_boi'), # LINHA NOVA
    
    # Assinatura (Protegido)
    path('assinatura/', views.assinatura, name='assinatura'),
]