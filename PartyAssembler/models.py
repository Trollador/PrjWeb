from django.db import models

# Create your models here.
class Registro_usuario(models.Model):
 email=models.CharField(max_length=200, default='E-mail')
 nome=models.CharField(max_length=50, default='Nome')
 senha=models.CharField(max_length=10, default='Senha')

class Perfil_usuario(models.Model):
 dta_nasc=models.DateTimeField
 nicks=models.TextField
 extras=models.TextField
 apelido=models.CharField(max_length=20, default='Apelido')
 nme_reg_usr=models.ForeignKey(Registro_usuario)
 
class Jogos(models.Model):
 nome=models.CharField(max_length=50, default='Nome')
 img=models.ImageField 
 
class ta_joga (models.Model):
 nome_jogo=models.ForeignKey(Jogos)
 apelido_pf_usr=models.ForeignKey(Perfil_usuario)
 rank=models.IntegerField()
 nivel=models.IntegerField()
 #id_joga=models.IntegerField()
 
class Times(models.Model):
 nome=models.CharField(max_length=50, default='Nome')
 descricao= models.TextField

class Participa(models.Model):
# id_part=models.IntegerField(default='1')
 apelido_usr=models.ForeignKey(Perfil_usuario)
 nme_time=models.ForeignKey(Times)
 


