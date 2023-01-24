from django.db import models
from tipo_transacao.models import TipoTransacao
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.
# é necessário fazer uma validação do cpf onde se aceita 11 dígitos e apenas os 11 dígitos
#ou seja, é necessário fazer uma validação onde o mínimo seja 11 e o máximo seja 11 também 
# 

def upload_file(instance,filename):


    print(f'o valor de filename é {filename}') 
    print(f'o valor do cnab é {CNABS}')




class CNABS(models.Model):

    document = models.FileField(upload_to=upload_file, blank=True, null=True)
    id_tipo_transacao = models.OneToOneField(TipoTransacao, related_name="id_tipo_transacao",on_delete=models.CASCADE)
    data  = models.DateField()
    valor = models.CharField()
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11), MaxLengthValidator(11)])
    cartao = models.CharField(max_length=12)
    hora = models.DateField()
    dono = models.CharField(max_length=14)
    nomeLoja = models.CharField(max_length=19)
    