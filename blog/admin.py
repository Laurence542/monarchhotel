from django.contrib import admin
from .models import Post, Services
from .models import Signup,Booking,Visitor,Visitor,Contact_us_info,Site_Information
from .import models



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


from .models import Visitor


admin.site.register(Site_Information)
admin.site.register(Post, PostAdmin)
admin.site.register(Signup)
admin.site.register(Contact_us_info)
admin.site.register(Services)
admin.site.register(Booking)
admin.site.register(Visitor)
admin.site.register(models.Category)


