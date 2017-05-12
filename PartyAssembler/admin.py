from django.contrib import admin
from .models import Registro_usuario
from .models import Perfil_usuario
from .models import Jogos
from .models import ta_joga
from .models import Participa
from .models import Times


admin.site.register(Registro_usuario)
admin.site.register(Perfil_usuario)
admin.site.register(Jogos)
admin.site.register(ta_joga)
admin.site.register(Participa)
admin.site.register(Times)


# Register your models here.
