from django.contrib import admin
from django.utils.html import mark_safe

from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    readonly_fields = ['image_tag']
    fieldsets = [
        ("Event Info", {"fields": ["image_tag", "image", "title", "description", "email", "dial_code", "contact"]}),
        ("Event Date", {"fields": ["date_start", "date_end"]}),
    ]
    list_display = ["title", "date_start", "date_created", "was_published_recently"]

    def image_tag(self, obj):
        return mark_safe('<img src="{}" width="300" height="300" />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

admin.site.register(Event, EventAdmin)