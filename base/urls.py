"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# project-level urls.py
from django.contrib import admin
from django.urls import include, path
from api.models import CourseResource, CategoryResource
from tastypie.api import Api

course_resource = CourseResource()
category_resource = CategoryResource()
api = Api(api_name="v1.0.0")

api.register(course_resource)
api.register(category_resource)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("shop/", include("shop.urls", namespace="courses")),
    # path("api/", include(category_resource.urls)),
    # path("api/", include(course_resource.urls)),
    # instead of the above ones, we will use the api because they are registered there
    path("api/", include(api.urls)),
]
