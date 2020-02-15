from django.contrib import admin
from .models import portalUser, UserLink, Token,Team
admin.site.register(portalUser)
admin.site.register(UserLink)
admin.site.register(Token)
admin.site.register(Team)
# Register your models here.
