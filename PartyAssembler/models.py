from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    return "%s%s" %(instance.id, filename)

# Create your models here.
class User_profile(models.Model):
    nickname = models.CharField(max_length = 20, default = "Nickname", primary_key = True)
    tags = models.TextField(default = "Tags")
    description = models.TextField(default = "Description")
    profile_img = models.ImageField(upload_to = upload_location,
    null = True,
    blank = True,
    width_field = "width_field",
    height_field = "height_field")
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)

class Party(models.Model):
    name=models.CharField(max_length = 50, default = "", primary_key = True)
    description = models.TextField(default = "")
    party_img = models.ImageField(upload_to = upload_location,
    null = True,
    blank = True,
    width_field = "width_field",
    height_field = "height_field")
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)

class Participate(models.Model):
    usr_nickname = models.ForeignKey(User_profile)
    party_name = models.OneToOneField(Party)

class Create(models.Model):
    usr_nickname = models.ForeignKey(User_profile)
    party_name = models.ForeignKey(Party)

class Game(models.Model):
    name = models.CharField(max_length = 50, default = "Name")
    game_cover = models.ImageField(upload_to = upload_location,
    null = True,
    blank = True,
    width_field = "width_field",
    height_field = "height_field")
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)

class Ta_Game_User (models.Model):
    game_name = models.ForeignKey(Game)
    user_nickname = models.ForeignKey(User_profile)
    rank = models.IntegerField()
    level=models.IntegerField()
