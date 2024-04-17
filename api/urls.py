from django.urls import include, path
from api.models import CourseResource, CategoryResource
from tastypie.api import Api

course_resource = CourseResource()
category_resource = CategoryResource()
api = Api(api_name="v1.0.0")


api.register(course_resource)
api.register(category_resource)

urlpatterns = [path("", include(api.urls))]
