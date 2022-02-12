from django.contrib import admin

from blog.models import blogpost, blogpostForm, Comments, profile

# Register your models here.
admin.site.register(profile)
admin.site.register(blogpost)
admin.site.register(Comments)