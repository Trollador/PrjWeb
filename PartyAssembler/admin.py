from django.contrib import admin
from .models import User_profile
from .models import Party
from .models import Participate
from .models import Create
from .models import Game
from .models import Ta_Game_User

# Register your models here.

admin.site.register(User_profile)
admin.site.register(Party)
admin.site.register(Participate)
admin.site.register(Create)
admin.site.register(Game)
admin.site.register(Ta_Game_User)
