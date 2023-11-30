from django.contrib import admin
from .models import Pessoa, PessoaFisica, PessoaJuridica, Telefone, Usuario, Cartao, Pedido, HistoricoStatus, Status, InformacaoEnvio, Endereco, ItemPedido, Produto, Categoria
# Register your models here.

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'saldo_conta')

@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'data_nascimento', 'sexo', 'rg')

@admin.register(PessoaJuridica)
class PessoaJuridicaAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'titulo_estabelecimento', 'codigo_descricao_atividade_economica')

@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'numero')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'email', 'perfil', 'numero_usuario')

@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'numero_cartao', 'nome_impresso', 'data_vencimento')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'data', 'valor_total', 'valor_desconto')

@admin.register(HistoricoStatus)
class HistoricoStatusAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'data')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(InformacaoEnvio)
class InformacaoEnvioAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'valor_frete', 'forma_envio', 'prazo_entrega')

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'municipio', 'UF', 'pais', 'referencia')

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'produto', 'qtde', 'preco')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cod_barras', 'preco', 'descricao', 'tamanho', 'avaliacao', 'categoria', 'imagem')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'filtros')