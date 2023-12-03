from django.db.models import Q
from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Produto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegistroForm


class IndexView(TemplateView):
    template_name = 'index.html'

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

class RegistroView(View):
    template_name = 'registro.html'

    def get(self, request):
        form = RegistroForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        return render(request, self.template_name, {'form': form})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'detalhes_produto.html', {'produto': produto})

def carrinho(request):
    # Adicione lógica para recuperar os produtos no carrinho (pode ser armazenado na sessão)
    produtos_no_carrinho = request.session.get('carrinho', [])

    # Recupere os detalhes dos produtos no carrinho do banco de dados
    produtos_detalhes = Produto.objects.filter(pk__in=produtos_no_carrinho)

    context = {
        'produtos_carrinho': produtos_detalhes,
    }

    return render(request, 'carrinho.html', context)

class SearchProdutosView(TemplateView):
    template_name = 'lista_produtos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')

        if query:
            # Realiza a pesquisa e filtra os produtos
            context['produtos'] = Produto.objects.filter(
                Q(nome__icontains=query) | Q(descricao__icontains=query)
            )
        else:
            # Se não houver consulta, exibe todos os produtos
            context['produtos'] = Produto.objects.all()

        return context