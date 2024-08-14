from django.contrib import admin

from .models import Event

# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["image", "title", "description", "email", "dial_code", "contact"]}),
        ("Event Date", {"fields": ["date_start", "date_end"]}),
    ]
    list_display = ["title", "date_start", "date_created", "was_published_recently"]


admin.site.register(Event, EventsAdmin)