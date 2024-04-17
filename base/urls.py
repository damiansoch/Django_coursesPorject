from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", include("shop.urls", namespace="courses")),
    path(
        "<path:unmatched>", RedirectView.as_view(url="", permanent=False)
    ),  # Redirect all unmatched paths to /shop/
    # path("api/", include(category_resource.urls)),
    # path("api/", include(course_resource.urls)),
    # instead of the above ones, we will use the api because they are registered there
    # path("api/", include(api.urls)),
    # and now we moved the url's to api url's
]
