from django.contrib import admin
from django.contrib.admin import register, ModelAdmin
from .models import Advice, Review, Teacher


@register(Advice)
class AdviceAdmin(ModelAdmin):
    list_display = (
        "name",
        "pub_date",
    )
    search_fields = ("name",)
    list_filter = ("name",)


@register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = (
        "name",
        "course",
        "teacherOrCourse",
        "pub_date"
    )
    search_fields = ("name",)
    list_filter = ("name", "course", "teacherOrCourse",)


@register(Teacher)
class TeacherAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
