from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from .views import IndexView, lista_produtos, detalhes_produto, carrinho, RegistroView, SearchProdutosView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('lista_produtos/', lista_produtos, name='lista_produtos'),
    path('produto/<int:produto_id>/', detalhes_produto, name='detalhes_produto'),
    path('carrinho/', carrinho, name='carrinho'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search_produto', SearchProdutosView.as_view(), name="search_produto")
]
