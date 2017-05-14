from django.db import models

# Create your models here.
class Registro_usuario(models.Model):
 email=models.CharField(max_length=200, default="E-mail")
 nome=models.CharField(max_length=50, default="Name")
 senha=models.CharField(max_length=10, default="Password")
 dta_nasc=models.CharField(max_length=10, default="Date")
 nicks=models.TextField(default="Nicknames")
 extras=models.TextField(default="Extras")
 apelido=models.CharField(max_length=20, default="Nickname")

class Jogos(models.Model):
 nome=models.CharField(max_length=50, default='Nome')
 img=models.ImageField

class ta_joga (models.Model):
 nome_jogo=models.ForeignKey(Jogos)
 apelido_pf_usr=models.ForeignKey(Registro_usuario)
 rank=models.IntegerField()
 nivel=models.IntegerField()
 #id_joga=models.IntegerField()

class Times(models.Model):
 nome=models.CharField(max_length=50, default='Nome')
 descricao= models.TextField
 foto_perfil=models.FileField

class Participa(models.Model):
# id_part=models.IntegerField(default='1')
 apelido_usr=models.ForeignKey(Registro_usuario)
 nme_time=models.ForeignKey(Times)
