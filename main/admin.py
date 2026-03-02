from django.contrib import admin
from .models import Case, CaseImage

class CaseImageInline(admin.TabularInline):
    model = CaseImage
    extra = 1
    fields = ("image", "scale", "caption", "sort")
    ordering = ("sort",)

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    inlines = [CaseImageInline]
    list_display = ("title", "slug", "is_published", "sort", "updated_at")
    list_editable = ("is_published", "sort")
    search_fields = ("title", "slug", "subtitle", "description")
    ordering = ("sort", "-updated_at")
    fieldsets = (
        (None, {"fields": ("title", "slug", "subtitle", "description")}),
        ("Публикация", {"fields": ("is_published", "sort")}),
    )