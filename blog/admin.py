from django.contrib import admin
from .models import Post, Profile, Images, Comment,Report
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','body','created','updated','status')
    list_filter = ('status', 'created', 'updated')
    search_fields = ('author__username', 'title')
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'dob','mob','city','photo')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id','post','image')
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id','req', 'user', 'post','cmnt','reason','body')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','post', 'user','reply','content','timestamp')

admin.site.register(Comment,CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Report,ReportAdmin)
