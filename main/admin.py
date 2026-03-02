# main/admin.py
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
    list_filter = ("is_published",)
    search_fields = ("title", "subtitle", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("created_at",)

    fieldsets = (
        ("Основное", {"fields": ("title", "slug", "subtitle", "description", "is_published", "sort")}),
        ("Картинки страницы", {"fields": ("cover_image", "hero_image", "mockup_image")}),
        ("Тексты блоков", {"fields": ("task_text", "execution_text", "result_text")}),
        ("Desktop / Mobile", {"fields": ("desktop_text", "desktop_image", "mobile_text", "mobile_image")}),
    )