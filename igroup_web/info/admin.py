# coding: utf-8

from django.contrib import admin
from info.models import org,group,person

class OrgAdmin(admin.ModelAdmin):
	pass
    #list_display = ('name', 'des', 'password')

class GroupAdmin(admin.ModelAdmin):
	pass
    #list_display = ('name', 'des', 'org')

class PersonAdmin(admin.ModelAdmin):
	pass
    #list_display = ('name', 'title', 'group', 'phone_number', 'mail', 'qq', 'weibo', 'birthday')

admin.site.register(org, OrgAdmin)
admin.site.register(group, GroupAdmin)
admin.site.register(person, PersonAdmin)
