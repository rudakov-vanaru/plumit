# main/admin.py
from django.contrib import admin
from .models import Case, CaseImage
from django.utils.html import format_html


class CaseImageInline(admin.TabularInline):
    model = CaseImage
    extra = 1
    fields = ("image", "scale", "title", "subtitle", "sort")
    ordering = ("sort",)


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    inlines = [CaseImageInline]
    list_display = ("title", "slug", "is_published", "sort", "updated_at")
    list_filter = ("is_published",)
    search_fields = ("title", "subtitle", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("created_at",)
    readonly_fields = ("cover_preview",)

    fieldsets = (
        ("Основное", {"fields": ("title", "slug", "subtitle", "description", "is_published", "sort")}),
        ("Картинки страницы", {"fields": ("cover_image", "cover_scale", "cover_preview", "hero_image", "mockup_image")}),
        ("Тексты блоков", {"fields": ("task_text", "execution_text", "result_text")}),
        ("Desktop / Mobile", {"fields": ("desktop_text", "desktop_image", "mobile_text", "mobile_image")}),
    )
    
    @admin.display(description="Превью обложки")
    def cover_preview(self, obj: Case):
        if not obj or not obj.cover_image:
            return ""
        scale = getattr(obj, "cover_scale", 100) or 100
        return format_html(
            '<img id="cover-preview-img" src="{}" style="width:{}%; max-width: 100%; height: auto; border-radius: 12px;" />',
            obj.cover_image.url,
            scale,
        )
    
    class Media:
        js = ("admin/js/case_cover_preview.js",)

