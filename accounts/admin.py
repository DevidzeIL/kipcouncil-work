from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Specialty)
admin.site.register(Company)

admin.site.register(Student)
admin.site.register(UserFunction)
admin.site.register(UserAward)
admin.site.register(UserComment)

admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(Member)
admin.site.register(New)
admin.site.register(About)
admin.site.register(ListDirection)

admin.site.register(DocsName)
admin.site.register(DocsCollege)
admin.site.register(DocsCouncil)