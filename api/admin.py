from django.contrib import admin  # type: ignore[import]
from .models import Students, Frame
# Register your models here.


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'studentName', 'studentEmail']


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    list_display = ['id', 'frame_name', 'frame_type',
                    'frame_comment', 'frame_image']
