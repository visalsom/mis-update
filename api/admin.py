from django.contrib import admin

from api.models import Department, Send, Soldier,Document, Subdepartment, Unit

# Register your models here.
admin.site.register(Document)
admin.site.register(Soldier)
admin.site.register(Unit)
admin.site.register(Department)
admin.site.register(Subdepartment)
admin.site.register(Send)
