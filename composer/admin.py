from django.contrib import admin
from .models import Composition

@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "style", "favorite", "created_at")
    list_filter = ("style", "favorite")
    search_fields = ("title", "user__username")
