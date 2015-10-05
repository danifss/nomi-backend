from django.contrib import admin
from .models import Attribute, Profile

class AttributeAdmin(admin.ModelAdmin):
    model = Attribute

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    filter_horizontal = ('connections', 'attributes',)

# class ProfileAttributeAdmin(admin.ModelAdmin):
#     model = ProfileAttribute

admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Profile, ProfileAdmin)
#admin.site.register(ProfileAttribute, ProfileAttributeAdmin)