from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Produto
from .filters import ProdutoFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import RegistroForm


class IndexView(TemplateView):
    template_name = 'index.html'

class lista_produtos(TemplateView):
    template_name = 'lista_produtos.html'

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

def lista_produtos(request):
    produto_filter = ProdutoFilter(request.GET, queryset=Produto.objects.all())
    return render(request, 'lista_produtos.html', {'filter': produto_filter})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'detalhes_produto.html', {'produto': produto})

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

