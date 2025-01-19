from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ProfessionalExperience, Testimony


@admin.register(ProfessionalExperience)
class ProfessionalExperienceAdmin(admin.ModelAdmin):
    list_display = ('about', 'proof_link')


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'message', 'avatar')
    search_fields = ('author_name', 'message')
    list_filter = ('author_name',)

    def avatar_preview(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="50" height="50" />')
        return "-"
    avatar_preview.short_description = "Aperçu Avatar"
