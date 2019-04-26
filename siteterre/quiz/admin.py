from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import PlayerGroup, Player, Question

# Register custom models
admin.site.register(PlayerGroup)
admin.site.register(Player)
admin.site.register(Question)

# Unregister the default models so they don't show up in the admin page
admin.site.unregister(User)
admin.site.unregister(Group)
