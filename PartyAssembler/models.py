from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def upload_location(instance, filename):
    return "%s%s" %(instance.id, filename)

# Create your models here.
class User_profile(models.Model):
    idt = models.OneToOneField(User, default = 1)
    tags = models.TextField(default = "Tags")
    description = models.TextField(default = "Description")
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
    width_field = models.IntegerField(default = 270)
    height_field = models.IntegerField(default = 380)


class Party(models.Model):
    name=models.CharField(max_length = 50, default = "")
    description = models.TextField(default = "")
    leader = models.ForeignKey(User, default = 1)
    related_game = models.ForeignKey(Game, related_name='related_game', default = 1)
    party_img = models.ImageField(upload_to = upload_location,
    null = True,
    blank = True,
    width_field = "width_field",
    height_field = "height_field")
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)

class Enter_party(models.Model):
    party_has_users = models.ForeignKey(User, default = 1)
    user_has_parties = models.ForeignKey(Party, default = 1)

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message
