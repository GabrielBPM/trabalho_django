from django.db import models
# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    saldo_conta = models.DecimalField(max_digits=10, decimal_places=2)

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1)
    rg = models.CharField(max_length=20)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=18)
    titulo_estabelecimento = models.CharField(max_length=100)
    codigo_descricao_atividade_economica = models.CharField(max_length=10)

class Telefone(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)

class Usuario(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    senha = models.CharField(max_length=100)
    email = models.EmailField()
    favoritos = models.ManyToManyField('Produto')
    perfil = models.CharField(max_length=100)
    numero_usuario = models.IntegerField()

class Cartao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numero_cartao = models.CharField(max_length=16)
    nome_impresso = models.CharField(max_length=100)
    data_vencimento = models.DateField()

class Pedido(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    valor_desconto = models.DecimalField(max_digits=10, decimal_places=2)

class HistoricoStatus(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    data = models.DateField()

class Status(models.Model):
    nome = models.CharField(max_length=100)

class InformacaoEnvio(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    valor_frete = models.DecimalField(max_digits=10, decimal_places=2)
    forma_envio = models.CharField(max_length=100)
    prazo_entrega = models.IntegerField()

class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    UF = models.CharField(max_length=2)
    pais = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100, blank=True, null=True)

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    qtde = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    cod_barras = models.CharField(max_length=20)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    tamanho = models.CharField(max_length=10)
    indicacao_uso = models.TextField()
    avaliacao = models.DecimalField(max_digits=3, decimal_places=2)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    filtros = models.TextField()
