from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category

admin.site.register(Post)
admin.site.register(Category)

#@admin.register(Post)
#class PostAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(Post, PostAdmin)

#@admin.register(Category)
#class CategoryAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(Post, PostAdmin)

class MembershipInline(admin.TabularInline):
    model = Post.categories.through

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]

class PostAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ('categories',)
