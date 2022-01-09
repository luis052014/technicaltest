from django.contrib import admin
from .models import ProfileAdmin, Product,ProfileSeller
# Register your models here.
admin.site.register(ProfileAdmin)
admin.site.register(Product)
admin.site.register(ProfileSeller)