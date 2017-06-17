from django.contrib import admin
from .models import User_profile
from .models import Party
from .models import Game
from .models import Enter_party

# Register your models here.

admin.site.register(User_profile)
admin.site.register(Party)
admin.site.register(Game)
admin.site.register(Enter_party)
