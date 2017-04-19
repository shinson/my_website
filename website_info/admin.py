from django.contrib import admin
from .models import *
# Register your models here.
class MediaAdmin(admin.ModelAdmin):
	pass

class ProjectAdmin(admin.ModelAdmin):
    pass

class SkillAdmin(admin.ModelAdmin):
    pass

class SkillAdmin(admin.ModelAdmin):
    pass

class WorkAdmin(admin.ModelAdmin):
    pass

admin.site.register(Media, MediaAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Work, WorkAdmin)