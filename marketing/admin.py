from django.contrib import admin
from .models import Signup
# Register your models here.
class SignAdmin(admin.ModelAdmin):
    list_display = ('id', 'email','timestamp')
    list_display_links = ('id', 'email')
    
    search_fields = ('email',)
admin.site.register(Signup,SignAdmin)