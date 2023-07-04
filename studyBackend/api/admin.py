from django.contrib.admin import register, ModelAdmin

from .models import Advice, FAQ, Review, Teacher


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


@register(FAQ)
class FAQAdmin(ModelAdmin):
    list_display = ("question",)
    search_fields = ("question",)
    list_filter = ("question",)
