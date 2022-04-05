from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'details','date')
    list_filter = ('name', 'date')
    search_fields = ('name', 'details')

    class Meta:
        model = Feedback


admin.site.register(Feedback, FeedbackAdmin)
