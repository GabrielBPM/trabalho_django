from django.db import models
# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, null=False)
    saldo_conta = models.DecimalField(max_digits=10, decimal_places=2)

class PessoaFisica(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, null=False)
    data_nascimento = models.DateField(null=False)
    sexo = models.CharField(max_length=1)
    rg = models.CharField(max_length=20, null=False)

class PessoaJuridica(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=18, null=False)
    titulo_estabelecimento = models.CharField(max_length=100, null=False)
    codigo_descricao_atividade_economica = models.CharField(max_length=10)

class Telefone(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20, null=False)

class Usuario(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    senha = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    favoritos = models.ManyToManyField('Produto')
    perfil = models.CharField(max_length=100)
    numero_usuario = models.IntegerField(null=False)

class Cartao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numero_cartao = models.CharField(max_length=16, null=False)
    nome_impresso = models.CharField(max_length=100, null=False)
    data_vencimento = models.DateField(null=False)

class Pedido(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data = models.DateField(null=False)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    valor_desconto = models.DecimalField(max_digits=10, decimal_places=2)

class HistoricoStatus(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    data = models.DateField(null=False)

class Status(models.Model):
    nome = models.CharField(max_length=100)

class InformacaoEnvio(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    valor_frete = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    forma_envio = models.CharField(max_length=100)
    prazo_entrega = models.IntegerField(null=False)

class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cep = models.CharField(max_length=10, null=False)
    logradouro = models.CharField(max_length=100, null=False)
    numero = models.CharField(max_length=10, null=False)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, null=False)
    municipio = models.CharField(max_length=100, null=False)
    UF = models.CharField(max_length=2, null=False)
    pais = models.CharField(max_length=100, null=False)
    referencia = models.CharField(max_length=100, blank=True, null=True)

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    qtde = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False)
    cod_barras = models.CharField(max_length=20, null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    descricao = models.TextField()
    tamanho = models.CharField(max_length=10)
    indicacao_uso = models.TextField(null=False)
    avaliacao = models.DecimalField(max_digits=3, decimal_places=2, null=False)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.TextField(null=False)
    filtros = models.TextField()
