from django.contrib import admin
from . models import (
    UserProfile,
    ContactProfile,
    Testimonial,
    Media,
    Blog,
    Certificate,
    Skill
    )
# Register your models here.

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ('id','user')
    
@admin.register(ContactProfile)
class ContactProfile(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(Testimonial)
class Testimonial(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    
@admin.register(Media)
class Media(admin.ModelAdmin):
    list_display = ('id','name')
    
    
@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)
    
    
@admin.register(Skill)
class Skill(admin.ModelAdmin):
    list_display = ('id','name','score')
    
@admin.register(Certificate)
class Certificate(admin.ModelAdmin):
    list_display = ('id','name')