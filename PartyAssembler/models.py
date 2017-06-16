from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def upload_location(instance, filename):
    return "%s%s" %(instance.id, filename)

# Create your models here.
class User_profile(models.Model):
    idt = models.OneToOneField(User, default = 1)
    profile_img = models.ImageField(upload_to = upload_location,
    null = True,
    blank = True,
    width_field = "width_field",
    height_field = "height_field")
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)


class Game(models.Model):
    name = models.CharField(max_length = 50, default = "Name")
    game_cover = models.ImageField(upload_to = upload_location,
    null = True,
    blank = True,
    width_field = "width_field",
    height_field = "height_field")
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)

class Party(models.Model):
    name=models.CharField(max_length = 50, default = "", primary_key = True)
    description = models.TextField(default = "")
    leader = models.OneToOneField(User, default = "")
    related_game = models.ForeignKey(Game, default = "") 
    party_img = models.ImageField(upload_to = upload_location,   
    null = True,
    blank = True,
    width_field = "width_field",
    height_field = "height_field")
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)

class Enter_party(models.Model):
    entry_date_time = models.DateTimeField(default=timezone.now())
    usr_nickname = models.ForeignKey(User)
    party_name = models.OneToOneField(Party)




