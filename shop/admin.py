from django.contrib import admin
from .models import Course, Category


# set up site titles and headers
admin.site.site_header = "Courses Admin"
admin.site.site_title = "My courses"
admin.site.index_title = "Welcome to the courses admin area"


# add other fields to the courses page in admin
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "category")


# adding courses to be visible in category
class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ["created_at"]
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    inlines = [CoursesInline]


# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
