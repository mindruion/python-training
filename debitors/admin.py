from django.contrib import admin

from debitors.models import Debitor


@admin.register(Debitor)
class DebitorAdmin(admin.ModelAdmin):
    pass
