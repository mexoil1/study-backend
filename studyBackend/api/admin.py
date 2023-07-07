from django.contrib.admin import register, ModelAdmin

from .models import Advice, Review, Teacher


@register(Advice)
class AdviceAdmin(ModelAdmin):
    list_display = (
        "pub_date",
    )


@register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = (
        "course",
        "teacherOrCourse",
        "pub_date"
    )
    search_fields = ("teacherOrCourse",)
    list_filter = ( "course", "teacherOrCourse",)


@register(Teacher)
class TeacherAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
