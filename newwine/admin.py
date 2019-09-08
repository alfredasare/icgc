from django.contrib import admin
from .models import *
from django.shortcuts import get_object_or_404
from multiupload.admin import MultiUploadAdmin


class ImageInlineAdmin(admin.TabularInline):
    model = Images


class GalleryMultiuploadMixing(object):

    def process_uploaded_file(self, uploaded, gallery, request):
        if gallery:
            image = gallery.images.create(file=uploaded)
        else:
            image = Images.objects.create(file=uploaded, gallery=None)
        return {
            'url': image.file.url,
            'thumbnail_url': image.file.url,
            'id': image.id,
            'name': image.filename
        }


class GalleryAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    inlines = [ImageInlineAdmin, ]
    multiupload_form = True
    multiupload_list = False

    def delete_file(self, pk, request):
        '''
        Delete an image.
        '''
        obj = get_object_or_404(Images, pk=pk)
        return obj.delete()


class ImageAdmin(GalleryMultiuploadMixing, MultiUploadAdmin):
    multiupload_form = False
    multiupload_list = True


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Images, ImageAdmin)
admin.site.register(Carousel)
admin.site.register(MainEvent)
admin.site.register(Quote)
admin.site.register(LatestSermons)
admin.site.register(Announcements)
admin.site.register(Theme)
admin.site.register(Testimonies)
admin.site.register(Notes)
admin.site.register(Outlines)
admin.site.register(Articles)
admin.site.register(Coordinator)
admin.site.register(Gender)
admin.site.register(Teams)
admin.site.register(ExecutivesThumbnail)
admin.site.register(ExecutivesDetails)
admin.site.register(RegisteredMembers)
admin.site.register(Departments)
admin.site.register(Sermons)
admin.site.register(Family)
admin.site.register(Initiators)
